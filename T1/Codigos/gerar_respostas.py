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

from datetime import date
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

from google_agenda import consultar_agenda_real, criar_evento_real
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


def adicionar_tarefa(titulo: str, prazo: str, prioridade: str) -> str:
    tarefas = _carregar_tarefas_do_disco()
    
    # Define o próximo ID autoincrementado
    novo_id = max([t["id"] for t in tarefas], default=0) + 1
    
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "pendente"
    }
    
    tarefas.append(nova_tarefa)
    _salvar_tarefas_no_disco(tarefas)
    
    resposta = f"✅ Tarefa '{titulo}' gravada localmente com ID {novo_id} (Prazo: {prazo})."
    
    # INTEGRAÇÃO INTELIGENTE: Cria um aviso/compromisso na Agenda do Google automaticamente
    print(f"   🚀 Sincronizando prazo da tarefa com o Google Calendar...")
    resultado_google = criar_evento_real(
        titulo=f"🚨 PRAZO: {titulo}",
        data_str=prazo,
        descricao=f"Tarefa acadêmica registrada no Jarvis.\nPrioridade: {prioridade}\nStatus: Pendente"
    )
    
    return f"{resposta}\n[Sincronização Nuvem]: {resultado_google}"


def concluir_tarefa(id_tarefa: int) -> str:
    tarefas = _carregar_tarefas_do_disco()
    encontrada = False
    
    for t in tarefas:
        if t["id"] == int(id_tarefa):
            t["status"] = "concluida"
            encontrada = True
            titulo_tarefa = t["titulo"]
            prazo_tarefa = t["prazo"]
            break
            
    if not encontrada:
        return f"❌ Nenhuma tarefa com ID {id_tarefa} foi localizada."
        
    _salvar_tarefas_no_disco(tarefas)
    
    # Opcional: Adiciona uma marcação visual ou evento na agenda indicando a conclusão
    criar_evento_real(
        titulo=f"✅ CONCLUÍDO: {titulo_tarefa}",
        data_str=prazo_tarefa,
        descricao=f"Tarefa concluída com sucesso no ecossistema Jarvis!"
    )
    
    return f"✅ Tarefa '{titulo_tarefa}' marcada como concluída no banco local e atualizada na agenda!"


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
   - Uso: quando o usuário perguntar sobre eventos, aulas ou compromissos.
   - JSON: {"tool": "consultar_agenda", "args": {"data": "YYYY-MM-DD"}}

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

REGRAS:
- Use buscar_material_rag ANTES de responder qualquer pergunta sobre conteúdo das aulas.
- Quando acionar uma ferramenta, responda APENAS o JSON — sem texto antes ou depois.
- Após receber o resultado da ferramenta, formule a resposta final normalmente em português.
- Nunca invente dados de agenda, tarefas ou conteúdo — use sempre as ferramentas.
"""


# ============================================================
# EXECUTOR DE FERRAMENTAS
# ============================================================

def executar_ferramenta(nome: str, argumentos: dict, modelo_emb, indices) -> str:
    """Recebe o nome e os argumentos da tool call e executa a função correta."""
    print(f"   🔧 Tool acionada: {nome}({argumentos})")

    # 1. Executa a ferramenta e guarda o resultado na variável
    if nome == "consultar_agenda":
        resultado = consultar_agenda_real(**argumentos)
    elif nome == "listar_tarefas":
        resultado = listar_tarefas(**argumentos)
    elif nome == "adicionar_tarefa":
        resultado = adicionar_tarefa(**argumentos)
    elif nome == "concluir_tarefa":
        resultado = concluir_tarefa(**argumentos)
    elif nome == "buscar_material_rag":
        resultado = buscar_material_rag(argumentos["query"], modelo_emb, indices)
    else:
        resultado = f"Ferramenta '{nome}' não reconhecida."

    # 2. Grava o Log no disco (Requisito de Engenharia de Software)
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

{DESCRICAO_FERRAMENTAS}"""


# ============================================================
# GERADOR DE RESPOSTA (loop de tool calling)
# ============================================================

def _detectar_tool_call(texto: str):
    """
    Verifica se a resposta da LLM é um JSON de tool call.
    Retorna (nome, args) se for, ou (None, None) se não for.
    """
    texto = texto.strip()
    # Tenta extrair JSON mesmo que venha dentro de bloco ```json ... ```
    if texto.startswith("```"):
        linhas = texto.splitlines()
        texto = "\n".join(linhas[1:-1]).strip()
    try:
        dados = json.loads(texto)
        if "tool" in dados and "args" in dados:
            return dados["tool"], dados["args"]
    except (json.JSONDecodeError, TypeError):
        pass
    return None, None


def gerar_resposta(historico: list, modelo_emb, indices) -> str:
    """
    Recebe o histórico completo de mensagens e retorna a resposta do JARVIS.
    Usa tool calling manual: detecta JSON de ferramenta na resposta da LLM,
    executa, injeta o resultado e chama a LLM novamente até obter resposta final.
    """
    mensagens  = historico.copy()
    MAX_RODADAS = 5

    for rodada in range(MAX_RODADAS):
        resposta = client.chat.completions.create(
            model=MODEL_ID,
            messages=mensagens,
            max_tokens=MAX_TOKENS,
        )

        conteudo = resposta.choices[0].message.content.strip()
        nome_tool, args_tool = _detectar_tool_call(conteudo)

        # Sem tool call → resposta final
        if nome_tool is None:
            return conteudo

        # Com tool call → executa e injeta resultado no histórico
        print(f"   🔧 Tool chamada: {nome_tool}({args_tool})")
        resultado = executar_ferramenta(nome_tool, args_tool, modelo_emb, indices)

        # Adiciona a chamada da ferramenta e o resultado como mensagens
        mensagens.append({"role": "assistant", "content": conteudo})
        mensagens.append({
            "role":    "user",
            "content": f"[Resultado da ferramenta {nome_tool}]:\n{resultado}\n\nAgora responda ao usuário com base neste resultado."
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