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

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# CARREGA AS VARIÁVEIS DO ARQUIVO .env PARA A MEMÓRIA DO PYTHON
load_dotenv() 

PASTA_INDICES = os.getenv(r'PASTA_EMBEDDINGS')  # Pasta onde estão os índices FAISS e BM25
ARQUIVO_TAREFAS = "tarefas.json"

MODEL_ID      = "google/gemma-3-12b-it"
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
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it',
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

def buscar_material_rag(query: str, modelo, indices) -> str:
    resultados = buscar_hibrido(query, modelo, indices, top_k=TOP_K_RAG, peso_semantico=PESO_SEM)
    if not resultados:
        return "Nenhum material relevante encontrado para esta consulta."
    contexto = ""
    for i, r in enumerate(resultados, 1):
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

REGRAS:
- Use buscar_material_rag ANTES de responder sobre conteúdo.
- Quando acionar uma ferramenta, responda APENAS com o JSON no formato especificado.
- Se o usuário pedir duas ou mais coisas, você PODE e DEVE gerar os múltiplos JSONs na mesma resposta, um em cada linha.
- REGRA DE CONFIRMAÇÃO (APENAS PARA EXCLUIR EVENTOS DA AGENDA): Se o usuário pedir para deletar ou remover um evento do calendário, NUNCA chame 'remover_evento_agenda' de imediato. Você DEVE usar 'buscar_evento_por_titulo' primeiro, apresentar a data ao usuário e perguntar "Tem certeza que deseja remover?". Aguarde o "sim" para prosseguir.
- REGRA DE TAREFAS (SEM CONFIRMAÇÃO, AÇÃO IMEDIATA): NUNCA adivinhe o ID de uma tarefa. Se o usuário pedir para concluir ou deletar uma tarefa, use 'listar_tarefas' primeiro para descobrir o ID. ASSIM QUE O PYTHON DEVOLVER O ID, VOCÊ DEVE EMITIR O JSON DE 'concluir_tarefa' OU 'deletar_tarefa' IMEDIATAMENTE NA PRÓXIMA RODADA. NÃO peça confirmação e NÃO faça perguntas ao usuário sobre tarefas. Apenas execute.
- NUNCA afirme textualmente que uma tarefa ou evento foi criado, concluído ou deletado a menos que você tenha visto o resultado de sucesso da ferramenta correspondente nos logs do sistema.
- Nunca invente dados. Se não tiver certeza, diga que não encontrou a informação.
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
- Baseie respostas acadêmicas APENAS no contexto recuperado pelo RAG.
- Se o contexto não contiver a informação, diga claramente que não encontrou nos materiais.
- Incentive o aprendizado ativo: ao explicar um conceito, ofereça fazer perguntas de revisão.
- Seja objetivo mas completo. Evite respostas vagas.
-Se o usuário fizer uma pergunta que correlacione um conteúdo não especificado pelo contexto do rag com o conteúdo disponível, diga que apenas poderá responder sobre o que está presente nos materiais indexados, e sugira reformular a pergunta ou usar termos mais próximos do conteúdo.

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
            resultados_acumulados += f"[Resultado de {nome_tool}]:\n{resultado_execucao}\n\n"

        mensagens.append({
            "role": "user",
            "content": f"Resultados da execução:\n{resultados_acumulados.strip()}"
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