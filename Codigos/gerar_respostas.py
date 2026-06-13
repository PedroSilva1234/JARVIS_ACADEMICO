"""
gerar_resposta.py — Etapa 5 do pipeline RAG do JARVIS Acadêmico
================================================================
Integra tudo:
  - Busca híbrida (FAISS + BM25) via armazenar_vetores.py
  - Histórico de conversa (multi-turn)
  - Tool Calling (agenda, tarefas, RAG)
  - Geração de resposta via Gemma 12B (API compatível com OpenAI)

Dependências:
  pip install openai sentence-transformers faiss-cpu rank-bm25
  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

import json
import os
import logging
import re

from datetime import date
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

from google_agenda import (
    consultar_agenda_real, criar_evento_real, deletar_evento_real,
    criar_task_real, concluir_task_real, deletar_task_real,
    buscar_evento_por_titulo
)
from retrieval import IndicesRAG, buscar_hibrido
from Planejamento import montar_plano_estudos
from Aprendizado import iniciar_active_recall, gerar_exercicios, SessaoActiveRecall

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# CARREGA AS VARIÁVEIS DO ARQUIVO .env PARA A MEMÓRIA DO PYTHON
load_dotenv() 

PASTA_INDICES = os.getenv(r'PASTA_EMBEDDINGS')  # Pasta onde estão os índices FAISS e BM25
ARQUIVO_TAREFAS = "tarefas.json"
SESSAO_ACTIVE_RECALL = {}  # Armazena sessões de active recall por usuário (user_id -> SessaoActiveRecall)

MODEL_ID      = "Qwen/Qwen2.5-14B-Instruct-AWQ"
TOP_K_RAG     = 4       # chunks recuperados por busca
MAX_TOKENS    = 1024    # tamanho máximo da resposta
PESO_SEM      = 0.6     # peso semântico na busca híbrida

# ============================================================
# CONFIGURAÇÃO DE LOGS (Requisito Obrigatório)
# ============================================================
logging.basicConfig(
    filename='jarvis_tools.log',
    level=logging.INFO,
    format='%(asctime)s - JARVIS LOG - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
chave_api = os.getenv('LIA_API_KEY')

if not chave_api:
    print("🚨 ERRO: A chave da API não foi encontrada! Verifique o arquivo .env")

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq',
    api_key=chave_api
)

# ============================================================
# IMPLEMENTAÇÃO DAS FERRAMENTAS
# ============================================================


def _carregar_tarefas_do_disco() -> list:
    """Função auxiliar para ler o arquivo JSON local."""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    try:
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def _salvar_tarefas_no_disco(tarefas: list):
    """Função auxiliar para salvar a lista no arquivo JSON local."""
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


def listar_tarefas(status: str) -> str:
    tarefas = _carregar_tarefas_do_disco()
    filtradas = [t for t in tarefas if t["status"] == status]
    
    if not filtradas:
        return f"Nenhuma tarefa com status '{status}' encontrada no sistema."
        
    linhas = [f"  [{t['id']}] {t['titulo']} | Prazo: {t['prazo']} | Prioridade: {t['prioridade']}"
              for t in filtradas]
    return f"Tarefas {status}s no sistema local:\n" + "\n".join(linhas)

# ============================================================
# RE-IMPLEMENTAÇÃO DAS TAREFAS COM PERSISTÊNCIA REAL
# ============================================================
def adicionar_tarefa(titulo: str, prazo: str, prioridade: str) -> str:
    tarefas = _carregar_tarefas_do_disco()
    novo_id = max([t["id"] for t in tarefas], default=0) + 1
    
    print(f"   🚀 Criando tarefa real no Google Tasks...")
    # Cria no Google Tasks oficial
    resultado_tasks = criar_task_real(
        titulo=titulo,
        prazo_str=prazo,
        descricao=f"Prioridade: {prioridade} | Status: Pendente"
    )
    
    task_google_id = resultado_tasks.get("id") if resultado_tasks.get("sucesso") else None
    
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "pendente",
        "google_event_id": task_google_id  # Guardamos o ID do Tasks aqui
    }
    
    tarefas.append(nova_tarefa)
    _salvar_tarefas_no_disco(tarefas)
    
    status_nuvem = f"Sincronizado no Google Tasks (ID: {task_google_id})" if task_google_id else f"Erro na nuvem: {resultado_tasks.get('erro')}"
    return f"✅ Tarefa [{novo_id}] gravada no JSON.\n[Nuvem]: {status_nuvem}"


def concluir_tarefa(id_tarefa: int) -> str:
    """Atualiza o status da tarefa para concluída no JSON local e no Google Tasks."""
    tarefas = _carregar_tarefas_do_disco()
    
    # Cast preventivo para garantir que o ID seja tratado como inteiro puro
    id_alvo = int(float(id_tarefa))
    
    # Busca a tarefa correspondente dentro do arquivo local
    tarefa_encontrada = next((t for t in tarefas if t["id"] == id_alvo), None)
            
    if not tarefa_encontrada:
        return f"❌ Nenhuma tarefa com ID {id_tarefa} foi localizada no banco local."
        
    # 1. Atualiza o status no ecossistema local
    tarefa_encontrada["status"] = "concluida"
    _salvar_tarefas_no_disco(tarefas)
    
    # 2. Recupera a chave de sincronização da nuvem
    google_id = tarefa_encontrada.get("google_event_id")
    
    if google_id:
        print(f"   🚀 Sincronizando conclusão com o Google Tasks...")
        msg_google = concluir_task_real(google_id)
    else:
        msg_google = "Esta tarefa não possuía um ID de sincronização válido com a nuvem."
        
    return f"✅ Arquivo JSON atualizado! Tarefa [{id_alvo}] marcada como concluída.\n[Nuvem]: {msg_google}"

def consultar_agenda(data: str) -> str:
    return consultar_agenda_real(data)

SCORE_MINIMO_RAG = 0.3  # Chunks abaixo deste score são ignorados — sem conteúdo relevante

def buscar_material_rag(query: str, modelo, indices) -> str:
    resultados = buscar_hibrido(query, modelo, indices, top_k=TOP_K_RAG, peso_semantico=PESO_SEM)

    # Filtra resultados com score abaixo do mínimo
    relevantes = [r for r in resultados if r['score_final'] >= SCORE_MINIMO_RAG]

    if not relevantes:
        # Retorna tag especial que o gerar_resposta detecta para bloquear a LLM
        return "__SEM_CONTEXTO__"

    contexto = ""
    for i, r in enumerate(relevantes, 1):
        contexto += f"[Trecho {i} — {r['origem']} | score: {r['score_final']}]\n{r['texto']}\n\n"
    return contexto.strip()

def deletar_tarefa(id_tarefa: int) -> str:
    """Remove a tarefa do JSON local e do Google Tasks."""
    tarefas = _carregar_tarefas_do_disco()
    id_alvo = int(float(id_tarefa))
    tarefa_encontrada = next((t for t in tarefas if t["id"] == id_alvo), None)
    
    if not tarefa_encontrada:
        return f"❌ Nenhuma tarefa com ID {id_alvo} para remoção."
        
    # Remove da lista local
    tarefas = [t for t in tarefas if t["id"] != id_alvo]
    _salvar_tarefas_no_disco(tarefas)
    
    google_id = tarefa_encontrada.get("google_event_id")
    if google_id:
        msg_google = deletar_task_real(google_id)
    else:
        msg_google = "Removida apenas localmente."
        
    return f"✅ Tarefa [{id_alvo}] deletada do JSON.\n[Nuvem]: {msg_google}"

# ============================================================
# DESCRIÇÃO DAS FERRAMENTAS (tool calling manual via system prompt)
# ============================================================
# O servidor não suporta tool_choice="auto" da API OpenAI.
# Estratégia: instruímos o Gemma a responder em JSON estruturado
# quando precisar de uma ferramenta. O Python detecta e executa.

DESCRICAO_FERRAMENTAS = """
Você tem acesso às seguintes ferramentas. Quando precisar usá-las,
responda EXCLUSIVAMENTE com um JSON no formato abaixo, sem nenhum
texto adicional antes ou depois:

{"tool": "nome_da_ferramenta", "args": {argumentos}}

Ferramentas disponíveis:

1. consultar_agenda
1. consultar_agenda
   - Uso: quando o usuário perguntar sobre eventos, aulas, compromissos ou provas de um dia específico OU de um mês inteiro.
   - JSON: {"tool": "consultar_agenda", "args": {"data": "YYYY-MM-DD"}} para um dia, ou {"tool": "consultar_agenda", "args": {"data": "YYYY-MM"}} para ver o mês completo.

2. listar_tarefas
   - Uso: quando o usuário quiser ver tarefas pendentes ou concluídas.
   - JSON: {"tool": "listar_tarefas", "args": {"status": "pendente"}}
   - status pode ser: "pendente" ou "concluida"

3. adicionar_tarefa
   - Uso: quando o usuário quiser criar uma nova tarefa acadêmica.
   - JSON: {"tool": "adicionar_tarefa", "args": {"titulo": "...", "prazo": "YYYY-MM-DD", "prioridade": "alta"}}
   - prioridade pode ser: "alta", "media" ou "baixa"

4. concluir_tarefa
   - Uso: quando o usuário disser que finalizou uma tarefa.
   - JSON: {"tool": "concluir_tarefa", "args": {"id_tarefa": 1}}

5. buscar_material_rag
   - Uso: SEMPRE que o usuário perguntar sobre conteúdo acadêmico, conceitos ou fórmulas.
   - JSON: {"tool": "buscar_material_rag", "args": {"query": "termo ou pergunta"}}

6. adicionar_evento_agenda
   - Uso: para adicionar eventos, feriados ou lembretes (ex: aniversários) DIRETAMENTE na agenda do Google, que não sejam tarefas acadêmicas.
   - JSON: {"tool": "adicionar_evento_agenda", "args": {"titulo": "...", "data": "YYYY-MM-DD"}}

7. remover_evento_agenda
   - Uso: quando o usuário pedir expressamente para apagar, cancelar ou remover um evento ou lembrete da agenda do Google.
   - JSON: {"tool": "remover_evento_agenda", "args": {"titulo": "Nome do Evento"}}

8. deletar_tarefa
   - Uso: quando o usuário quiser excluir permanentemente uma tarefa do sistema.
   - JSON: {"tool": "deletar_tarefa", "args": {"id_tarefa": 1}}

9. buscar_evento_por_titulo
   - Uso: SEMPRE que o usuário pedir para remover um evento, use esta ferramenta ANTES para descobrir a data e o horário do evento.
   - JSON: {"tool": "buscar_evento_por_titulo", "args": {"titulo": "Nome do Evento"}}


10. montar_plano_estudos
   - Uso: quando o usuário pedir um plano de estudos, priorização do dia ou estratégia para uma prova.
   - JSON: {"tool": "montar_plano_estudos", "args": {"janela_dias": 7, "foco": ""}}
   - janela_dias: quantos dias à frente considerar (padrão 7)
   - foco: tema ou prova específica (deixe vazio "" para plano geral)

11. iniciar_active_recall
   - Uso: quando o usuário quiser ser testado, revisar ou praticar um tema com perguntas interativas.
   - JSON: {"tool": "iniciar_active_recall", "args": {"tema": "nome do tema"}}
   - REGRA DE BLOQUEIO (MUITO IMPORTANTE): Se o usuário disser apenas "me teste", "vamos revisar" ou "iniciar active recall" SEM especificar qual é o assunto exato na mesma frase, VOCÊ ESTÁ PROIBIDO DE ACIONAR ESTA FERRAMENTA. NÃO TENTE ADIVINHAR O TEMA. Em vez de chamar a ferramenta, responda apenas conversando com o usuário: "Sobre qual tema específico você gostaria de fazer o teste hoje?".
   - REGRA ESTRITA: Quando você finalmente acionar esta ferramenta com o tema correto, VOCÊ ESTÁ PROIBIDO de gerar qualquer texto adicional. Não faça perguntas, não apresente listas, não comente o resultado da ferramenta. Retorne APENAS o JSON da ferramenta e deixe que o sistema assuma o controle.

12. gerar_exercicios
   - Uso: SOMENTE quando o usuário pedir EXPLICITAMENTE exercícios, questões, quiz ou prática. Exemplos: "me dá exercícios sobre X", "quero praticar X", "gera um quiz". NUNCA use esta ferramenta ao explicar um conteúdo sem pedido direto.
   - JSON: {"tool": "gerar_exercicios", "args": {"tema": "nome do tema", "tipo": "misto", "quantidade": 3}}
   - tipo pode ser: "multipla_escolha", "verdadeiro_falso", "aberta", "misto"

REGRAS:
- Use buscar_material_rag ANTES de responder sobre conteúdo.
- NUNCA chame gerar_exercicios ou iniciar_active_recall automaticamente ao explicar um conteúdo. Estas ferramentas só devem ser acionadas quando o usuário pedir EXPLICITAMENTE (usar palavras como "exercício", "quiz", "me teste", "quero praticar", "active recall").
- Ao final de uma explicação de conteúdo, você PODE oferecer ao usuário a opção de praticar ("Quer fazer exercícios ou perguntas de revisão sobre este tema?"), mas NÃO acione a ferramenta sem confirmação.
- Quando acionar uma ferramenta, responda APENAS com o JSON no formato especificado.
- Se o usuário pedir duas ou mais coisas, você PODE e DEVE gerar os múltiplos JSONs na mesma resposta, um em cada linha.
- REGRA DE CONFIRMAÇÃO (APENAS PARA EXCLUIR EVENTOS DA AGENDA): Se o usuário pedir para deletar ou remover um evento do calendário, NUNCA chame 'remover_evento_agenda' de imediato. Você DEVE usar 'buscar_evento_por_titulo' primeiro, apresentar a data ao usuário e perguntar "Tem certeza que deseja remover?". Aguarde o "sim" para prosseguir.
- REGRA DE TAREFAS (SEM CONFIRMAÇÃO, AÇÃO IMEDIATA): NUNCA adivinhe o ID de uma tarefa. Se o usuário pedir para concluir ou deletar uma tarefa, use 'listar_tarefas' primeiro para descobrir o ID. ASSIM QUE O PYTHON DEVOLVER O ID, VOCÊ DEVE EMITIR O JSON DE 'concluir_tarefa' OU 'deletar_tarefa' IMEDIATAMENTE NA PRÓXIMA RODADA. NÃO peça confirmação e NÃO faça perguntas ao usuário sobre tarefas. Apenas execute.
- NUNCA afirme textualmente que uma tarefa ou evento foi criado, concluído ou deletado a menos que você tenha visto o resultado de sucesso da ferramenta correspondente nos logs do sistema.
- Nunca invente dados. Se não tiver certeza, diga que não encontrou a informação.
- REGRA DE CONTEÚDO PARA ACTIVE RECALL: Se o usuário pedir para ser testado ou praticar um tema, VOCÊ DEVE usar 'buscar_material_rag' para recuperar o conteúdo relevante ANTES de chamar 'iniciar_active_recall'. O conteúdo recuperado deve ser a base para as perguntas do active recall. NUNCA chame 'iniciar_active_recall' sem antes buscar o material relevante.
- Se o usuário quando pedir pra ser testado NÃO especificar um tema, peça para ele escolher um tema específico RELACIONADO com os conteúdos disponíveis para a sessão de active recall. Você DEVE listar os temas mais relevantes encontrados no RAG e pedir para ele escolher um. APENAS DEPOIS de o usuário escolher o tema, chame 'iniciar_active_recall' com esse tema específico.
"""


# ============================================================
# EXECUTOR DE FERRAMENTAS
# ============================================================

def executar_ferramenta(nome: str, argumentos: dict, modelo_emb, indices) -> str:
    """Recebe o nome e os argumentos da tool call e executa a função correta."""
    print(f"   🔧 Tool acionada: {nome}({argumentos})")

    # 1. Executa a ferramenta e guarda o resultado na variável
    if nome == "consultar_agenda":
        resultado = consultar_agenda_real(argumentos["data"])
    elif nome == "listar_tarefas":
        resultado = listar_tarefas(**argumentos)
    elif nome == "adicionar_tarefa":
        resultado = adicionar_tarefa(**argumentos)
    elif nome == "concluir_tarefa":
        resultado = concluir_tarefa(**argumentos)
    elif nome == "buscar_material_rag":
        resultado = buscar_material_rag(argumentos["query"], modelo_emb, indices)
    elif nome == "adicionar_evento_agenda":
        # Chama a agenda para eventos genéricos (sem ser tarefa)
        res_google = criar_evento_real(
            titulo=argumentos["titulo"], 
            data_str=argumentos["data"], 
            descricao="Adicionado pelo Jarvis"
        )
        if res_google.get("sucesso"):
            resultado = f"Evento '{argumentos['titulo']}' adicionado com sucesso à Agenda do Google."
        else:
            resultado = f"Falha ao adicionar na Agenda: {res_google.get('erro')}"
    elif nome == "remover_evento_agenda":
        resultado = deletar_evento_real(argumentos["titulo"])
    elif nome == "deletar_tarefa":
        resultado = deletar_tarefa(**argumentos)
    elif nome == "buscar_evento_por_titulo":
        resultado = buscar_evento_por_titulo(argumentos["titulo"])
    elif nome == "montar_plano_estudos":
        janela = int(argumentos.get("janela_dias", 7))
        foco   = argumentos.get("foco", "")
        contexto_plano = montar_plano_estudos(modelo_emb, indices, janela_dias=janela, foco=foco)
        resultado = contexto_plano
    elif nome == "iniciar_active_recall":
        tema = argumentos.get("tema", "").strip()
        
        # O GUARDRAIL: Se a IA tentou mandar um tema vazio ou muito genérico, o Python barra a criação da sessão.
        if not tema or tema.lower() in ["", "geral", "qualquer", "conteúdo", "matéria", "assunto"]:
            resultado = "AÇÃO BLOQUEADA PELO SISTEMA: O tema está vazio ou genérico. Peça desculpas ao usuário e pergunte EXATAMENTE qual assunto específico ele deseja revisar."
        else:
            # Se passou pelo bloqueio, cria a sessão normalmente
            sessao, primeira_pergunta = iniciar_active_recall(tema, modelo_emb, indices)
            SESSAO_ACTIVE_RECALL["atual"] = sessao
            resultado = primeira_pergunta
            
    elif nome == "gerar_exercicios":
        tema       = argumentos.get("tema", "")
        tipo       = argumentos.get("tipo", "misto")
        quantidade = int(argumentos.get("quantidade", 3))
        resultado  = gerar_exercicios(tema, modelo_emb, indices, tipo=tipo, quantidade=quantidade)
    else:
        resultado = f"Ferramenta '{nome}' não reconhecida."

    # 2. Grava o Log no disco
    mensagem_log = f"Ferramenta: {nome} | Entrada: {argumentos} | Saída: {resultado}"
    logging.info(mensagem_log)

    # 3. Retorna para o LLM
    return resultado

# ============================================================
# SISTEMA DE PROMPT
# ============================================================


def montar_system_prompt() -> str:
    hoje = date.today().isoformat()
    return f"""Você é o JARVIS Acadêmico, um assistente pessoal inteligente para estudos.
Data de hoje: {hoje}

Seu comportamento:
- Responda sempre em português, de forma clara e didática.
- Seja objetivo mas completo. Evite respostas vagas.
- Incentive o aprendizado ativo: ao explicar um conceito, ofereça fazer perguntas de revisão.

REGRAS ABSOLUTAS SOBRE CONTEÚDO ACADÊMICO (não podem ser violadas):
- Você APENAS responde perguntas acadêmicas com base nos trechos retornados pela ferramenta buscar_material_rag.
- Se o RAG não retornar trechos relevantes sobre o tema perguntado, você deve responder EXATAMENTE: "Não encontrei informações sobre '[tema]' nos materiais indexados. Só posso responder com base nos documentos disponíveis. Tente reformular a pergunta com termos da matéria."
- É PROIBIDO usar conhecimento próprio para complementar, explicar ou expandir respostas acadêmicas. Mesmo que você saiba a resposta, NÃO a forneça se não estiver nos documentos.
- NÃO diga frases como "posso fornecer uma explicação geral" ou "com base no meu conhecimento". Isso é alucinação e está PROIBIDO.
- Se os trechos do RAG forem parcialmente relevantes, responda apenas com o que está nos trechos e indique que o material disponível é limitado sobre o tema.

{DESCRICAO_FERRAMENTAS}"""


# ============================================================
# GERADOR DE RESPOSTA (loop de tool calling)
# ============================================================

def _detectar_tool_calls(texto: str) -> list:
    # Encontra todas as ocorrências que batem com o formato de ferramenta
    matches = re.finditer(r'\{\s*"tool"\s*:\s*"[^"]+"\s*,\s*"args"\s*:\s*\{[^{}]*\}\s*\}', texto)
    
    chamadas = []
    for match in matches:
        try:
            dados = json.loads(match.group(0))
            chamadas.append((dados["tool"], dados["args"]))
        except json.JSONDecodeError:
            continue
            
    return chamadas

def gerar_resposta(historico: list, modelo_emb, indices) -> str:
    """
    Loop de execução que suporta encadeamento dinâmico de ferramentas (Chaining).
    Permite que a IA use uma ferramenta para buscar dados e outra para agir logo em seguida.
    """
    mensagens = historico.copy()
    MAX_RODADAS = 5
 
    for rodada in range(MAX_RODADAS):
        resposta = client.chat.completions.create(
            model=MODEL_ID,
            messages=mensagens,
            max_tokens=MAX_TOKENS,
        )
 
        conteudo = resposta.choices[0].message.content.strip()
        chamadas = _detectar_tool_calls(conteudo)
 
        # Se não há mais ferramentas para chamar, este conteúdo é a resposta final para o usuário
        if not chamadas:
            return conteudo
 
        # Registra o comando de ferramenta da IA no histórico interno da rodada
        mensagens.append({"role": "assistant", "content": conteudo})
        
        resultados_acumulados = ""
 
        # Executa todas as ferramentas solicitadas nesta rodada
        for nome_tool, args_tool in chamadas:
            resultado_execucao = executar_ferramenta(nome_tool, args_tool, modelo_emb, indices)
 
            # BLOQUEIO ANTI-ALUCINAÇÃO: RAG sem contexto relevante → resposta direta sem passar pela LLM
            if nome_tool == "buscar_material_rag" and resultado_execucao == "__SEM_CONTEXTO__":
                query_usada = args_tool.get("query", "este tema")
                return (
                    f"Não encontrei informações sobre '{query_usada}' nos materiais indexados. "
                    f"Só posso responder com base nos documentos disponíveis. "
                    f"Tente reformular com termos da matéria."
                )
            # BLOQUEIO ACTIVE RECALL: Se iniciou a sessão, bloqueia a LLM de reescrever a saída
            if nome_tool == "iniciar_active_recall":
                # Interrompe imediatamente o loop da IA e devolve o texto bruto gerado pela classe Python
                return resultado_execucao
 
            resultados_acumulados += f"[Resultado de {nome_tool}]:\n{resultado_execucao}\n\n"
 
        mensagens.append({
            "role": "user",
            "content": (
                f"Resultados da execução:\n{resultados_acumulados.strip()}\n\n"
                f"IMPORTANTE: Responda APENAS com base nos resultados acima. "
                f"NÃO use conhecimento próprio para complementar."
            )
        })
 
    return "⚠️ Limite de rodadas de tool calling atingido. Tente reformular sua pergunta."


# ============================================================
# LOOP DE CONVERSA (interface de terminal)
# ============================================================

def iniciar_jarvis():
    print("⏳ Carregando modelo de embeddings e índices RAG...")
    modelo_emb = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    indices    = IndicesRAG(PASTA_INDICES)
    print("✅ JARVIS Acadêmico pronto!\n")
    print("=" * 55)
    print("  JARVIS Acadêmico — Digite 'sair' para encerrar")
    print("=" * 55)

    # Histórico começa com o system prompt
    historico = [
        {"role": "system", "content": montar_system_prompt()}
    ]

    while True:
        try:
            entrada = input("\nVocê: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Encerrando o JARVIS.")
            break

        if not entrada:
            continue
        if entrada.lower() in ("sair", "exit", "quit"):
            print("👋 Até logo!")
            break

        # Verifica se há uma sessão de active recall ativa
        if "atual" in SESSAO_ACTIVE_RECALL and not SESSAO_ACTIVE_RECALL["atual"].encerrada:
            sessao_ativa = SESSAO_ACTIVE_RECALL["atual"]
            
            # Envia a resposta direto para a classe de aprendizado (sem IA do Jarvis interferir)
            feedback = sessao_ativa.avaliar_resposta(entrada)
            
            # Atualiza o histórico para ficar coerente
            historico.append({"role": "user", "content": entrada})
            historico.append({"role": "assistant", "content": feedback})
            
            print(f"\nJARVIS: {feedback}")
            
            # Se a palavra 'parar' encerrou a sessão na linha acima, deletamos a sessão
            if sessao_ativa.encerrada:
                del SESSAO_ACTIVE_RECALL["atual"]
            continue

        # Adiciona a mensagem do usuário ao histórico
        historico.append({"role": "user", "content": entrada})

        print("\nJARVIS: ", end="", flush=True)
        resposta = gerar_resposta(historico, modelo_emb, indices)
        print(resposta)

        # Adiciona a resposta final ao histórico (mantém o contexto)
        historico.append({"role": "assistant", "content": resposta})


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    iniciar_jarvis()