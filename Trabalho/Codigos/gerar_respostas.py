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
"""

import json
import os
from datetime import date
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Importa os módulos já construídos
from retrieval import IndicesRAG, buscar_hibrido

# ============================================================
# CONFIGURAÇÃO
# ============================================================

PASTA_INDICES = r"C:\Programas\facul\IA\Trabalho\Documents\embeddings"
MODEL_ID      = "google/gemma-3-12b-it"
TOP_K_RAG     = 4       # chunks recuperados por busca
MAX_TOKENS    = 1024    # tamanho máximo da resposta
PESO_SEM      = 0.6     # peso semântico na busca híbrida

# CARREGA AS VARIÁVEIS DO ARQUIVO .env PARA A MEMÓRIA DO PYTHON
load_dotenv() 

# Agora sim ele vai encontrar a chave!
chave_api = os.getenv('LIA_API_KEY')

if not chave_api:
    print("🚨 ERRO: A chave da API não foi encontrada! Verifique o arquivo .env")

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it',
    api_key=chave_api
)
# ============================================================
# BANCO DE DADOS SIMULADO (substitua pela sua implementação real)
# ============================================================

AGENDA = {
    "2026-05-17": ["Aula de Métodos Numéricos - 14h", "Entrega do relatório - 23h59"],
    "2026-05-18": ["Prova de Cálculo - 08h"],
    "2026-05-20": ["Seminário de IA - 10h"],
}

TAREFAS = [
    {"id": 1, "titulo": "Estudar interpolação de Lagrange", "prazo": "2026-05-18", "prioridade": "alta",   "status": "pendente"},
    {"id": 2, "titulo": "Revisar regressão logística",      "prazo": "2026-05-20", "prioridade": "media",  "status": "pendente"},
    {"id": 3, "titulo": "Lista de exercícios de IA",        "prazo": "2026-05-15", "prioridade": "alta",   "status": "concluida"},
]


# ============================================================
# IMPLEMENTAÇÃO DAS FERRAMENTAS
# ============================================================

def consultar_agenda(data: str) -> str:
    eventos = AGENDA.get(data, [])
    if not eventos:
        return f"Nenhum evento encontrado para {data}."
    return f"Eventos em {data}:\n" + "\n".join(f"  • {e}" for e in eventos)


def listar_tarefas(status: str) -> str:
    filtradas = [t for t in TAREFAS if t["status"] == status]
    if not filtradas:
        return f"Nenhuma tarefa com status '{status}'."
    linhas = [f"  [{t['id']}] {t['titulo']} | Prazo: {t['prazo']} | Prioridade: {t['prioridade']}"
              for t in filtradas]
    return f"Tarefas {status}s:\n" + "\n".join(linhas)


def adicionar_tarefa(titulo: str, prazo: str, prioridade: str) -> str:
    novo_id = max(t["id"] for t in TAREFAS) + 1
    TAREFAS.append({"id": novo_id, "titulo": titulo, "prazo": prazo,
                    "prioridade": prioridade, "status": "pendente"})
    return f"✅ Tarefa '{titulo}' adicionada com ID {novo_id}, prazo {prazo}."


def concluir_tarefa(id_tarefa: int) -> str:
    for t in TAREFAS:
        if t["id"] == id_tarefa:
            t["status"] = "concluida"
            return f"✅ Tarefa '{t['titulo']}' marcada como concluída."
    return f"❌ Tarefa com ID {id_tarefa} não encontrada."


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
    print(f"   🔧 Tool: {nome}({argumentos})")

    if nome == "consultar_agenda":
        return consultar_agenda(**argumentos)
    elif nome == "listar_tarefas":
        return listar_tarefas(**argumentos)
    elif nome == "adicionar_tarefa":
        return adicionar_tarefa(**argumentos)
    elif nome == "concluir_tarefa":
        return concluir_tarefa(**argumentos)
    elif nome == "buscar_material_rag":
        return buscar_material_rag(argumentos["query"], modelo_emb, indices)
    else:
        return f"Ferramenta '{nome}' não reconhecida."


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