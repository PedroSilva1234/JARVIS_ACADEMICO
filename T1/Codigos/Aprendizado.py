"""
aprendizado.py — Módulo de Funcionalidades de Aprendizado do JARVIS Acadêmico
==============================================================================
Implementa duas funcionalidades educacionais interativas:

  1. Active Recall  — o JARVIS faz perguntas ao usuário, avalia as respostas
                      e sugere revisão quando necessário. (INTERATIVA)

  2. Geração de Exercícios — cria exercícios variados (múltipla escolha,
                             V/F, aberta) a partir dos materiais do RAG.

Integração com gerar_respostas.py:
  - Importar as funções e registrar as ferramentas no DESCRICAO_FERRAMENTAS:

    10. iniciar_active_recall
       - Uso: quando o usuário quiser ser testado, revisar ou praticar um tema.
       - JSON: {"tool": "iniciar_active_recall", "args": {"tema": "interpolação de Lagrange"}}

    11. gerar_exercicios
       - Uso: quando o usuário pedir exercícios, questões ou um quiz sobre um tema.
       - JSON: {"tool": "gerar_exercicios", "args": {"tema": "regressão linear", "tipo": "multipla_escolha", "quantidade": 3}}
       - tipo pode ser: "multipla_escolha", "verdadeiro_falso", "aberta", "misto"
       - quantidade: número de questões (padrão: 3, máximo: 5)
"""

import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from retrieval import buscar_hibrido

load_dotenv()

# ── Cliente LLM (mesmo do gerar_respostas.py) ────────────────
chave_api = os.getenv('LIA_API_KEY')  # Certifique-se de que esta variável de ambiente esteja definida no .env

if not chave_api:
    print("🚨 ERRO: A chave da API não foi encontrada no .env pelo módulo de Aprendizado!")
    
client = OpenAI(
    base_url='https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq',
    api_key=chave_api
)
MODEL_ID   = "Qwen/Qwen2.5-14B-Instruct-AWQ"
MAX_TOKENS = 1024


# ============================================================
# HELPER: CHAMADA SIMPLES À LLM
# ============================================================

def _chamar_llm(system: str, user: str) -> str:
    """Faz uma chamada simples à LLM sem histórico."""
    resposta = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user}
        ],
        max_tokens=MAX_TOKENS,
    )
    return resposta.choices[0].message.content.strip()


def _recuperar_contexto(tema: str, modelo_emb, indices_rag, top_k: int = 4) -> str:
    """Busca trechos relevantes do RAG para o tema solicitado."""
    resultados = buscar_hibrido(
        query=tema,
        modelo=modelo_emb,
        indices=indices_rag,
        top_k=top_k,
        peso_semantico=0.6
    )
    if not resultados:
        return ""
    return "\n\n".join(
        f"[{r['origem']}]\n{r['texto']}" for r in resultados
    )


# ============================================================
# FUNCIONALIDADE 1: ACTIVE RECALL (INTERATIVA)
# ============================================================

# ============================================================
# FUNCIONALIDADE 1: ACTIVE RECALL (LOOP INFINITO)
# ============================================================

class SessaoActiveRecall:
    def __init__(self, tema: str, modelo_emb, indices_rag):
        self.tema         = tema
        self.modelo_emb   = modelo_emb
        self.indices_rag  = indices_rag
        self.respostas    = []   
        self.perguntas_feitas = [] # Guarda o histórico para não repetir perguntas
        self.pergunta_atual = ""
        self.encerrada    = False

        # Recupera contexto do banco de dados
        self.contexto = _recuperar_contexto(tema, modelo_emb, indices_rag)

    def gerar_nova_pergunta(self) -> str:
        """Gera UMA única pergunta dinâmica baseada no contexto e no que já foi perguntado."""
        if not self.contexto:
            return f"Não encontrei material suficiente sobre '{self.tema}' para testar você."

        prompt_sistema = (
            "Você é um professor conduzindo uma sessão de active recall oral. "
            "Faça UMA ÚNICA pergunta direta e clara sobre o tema. "
            "NÃO faça introduções, NÃO inclua a resposta e NÃO use formatação LaTeX (\\[, \\], $, $$). "
            "Apenas escreva a pergunta."
        )
        
        evitar = "\n".join(f"- {p}" for p in self.perguntas_feitas) if self.perguntas_feitas else "Nenhuma."
        
        prompt_usuario = (
            f"Tema: {self.tema}\n"
            f"Perguntas que você JÁ FEZ (NÃO REPITA):\n{evitar}\n\n"
            f"Contexto dos materiais:\n{self.contexto}\n\n"
            "Gere a PRÓXIMA pergunta:"
        )

        pergunta = _chamar_llm(prompt_sistema, prompt_usuario)
        self.pergunta_atual = pergunta
        self.perguntas_feitas.append(pergunta)
        
        return pergunta

    def avaliar_resposta(self, resposta_usuario: str) -> str:
        """Avalia a resposta do usuário, gera o feedback e já emenda a próxima pergunta."""
        # 1. Verifica se o usuário quer parar o teste
        palavras_parada = ["parar", "chega", "encerrar", "sair", "fim", "stop"]
        if resposta_usuario.lower().strip() in palavras_parada:
            self.encerrada = True
            return "Sessão de Active Recall encerrada pelo usuário! 🎉\n\n" + self.relatorio_final()

        # 2. Avalia a resposta atual
        prompt_sistema = (
            "Você é um professor avaliando uma resposta. Seja direto. "
            "NÃO USE formatação LaTeX (como \\[, \\], \\frac, $$). Escreva matemática em texto simples. "
            "Estruture exatamente assim:\n"
            "✅ Acertos: ...\n"
            "❌ Lacunas: ...\n"
            "💡 Complemento: ...\n"
            "⭐ Avaliação: [Excelente / Boa / Parcial / Insuficiente]"
        )
        prompt_usuario = (
            f"Pergunta: {self.pergunta_atual}\n"
            f"Resposta do aluno: {resposta_usuario}\n"
            f"Gabarito (Contexto):\n{self.contexto}"
        )

        feedback = _chamar_llm(prompt_sistema, prompt_usuario)
        acerto = any(p in feedback.lower() for p in ["excelente", "boa", "correto"])

        self.respostas.append({
            "pergunta": self.pergunta_atual,
            "resposta_usuario": resposta_usuario,
            "feedback": feedback,
            "acerto": acerto
        })

        # 3. Gera a PRÓXIMA pergunta automaticamente
        nova_pergunta = self.gerar_nova_pergunta()
        n = len(self.perguntas_feitas)

        # 4. Monta o pacote final: Feedback + Linha + Nova Pergunta
        resposta_completa = (
            f"{feedback}\n\n"
            f"{'─' * 40}\n"
            f"🧠 *Pergunta {n}*:\n{nova_pergunta}\n\n"
            f"*(Digite sua resposta ou digite 'parar' para encerrar)*"
        )
        
        return resposta_completa

    def relatorio_final(self) -> str:
        """Gera um relatório de desempenho da sessão."""
        if not self.respostas:
            return "Nenhuma resposta registrada nesta sessão."

        total = len(self.respostas)
        acertos = sum(1 for r in self.respostas if r["acerto"])
        pct = int((acertos / total) * 100)

        linhas = [
            f"📊 *Relatório Final — Active Recall: {self.tema}*",
            f"Acertos: {acertos}/{total} ({pct}%)",
            "\nPontos que merecem revisão:"
        ]

        erros = False
        for r in self.respostas:
            if not r["acerto"]:
                linhas.append(f"  • {r['pergunta']}")
                erros = True
                
        if not erros:
            linhas.append("  • Nenhum! Você dominou o assunto. 🏆")

        return "\n".join(linhas)


def iniciar_active_recall(tema: str, modelo_emb, indices_rag) -> tuple:
    """Inicia a sessão de Active Recall com loop infinito."""
    sessao = SessaoActiveRecall(tema, modelo_emb, indices_rag)
    
    # Usa a função NOVA em vez da antiga 'proxima_pergunta'
    primeira_pergunta = sessao.gerar_nova_pergunta()

    texto_inicial = (
        f"🧠 *Sessão de Active Recall Iniciada: {tema}*\n\n"
        f"Pergunta 1:\n{primeira_pergunta}\n\n"
        f"*(Digite sua resposta ou digite 'parar' para encerrar)*"
    )
    
    return sessao, texto_inicial

# ============================================================
# FUNCIONALIDADE 2: GERAÇÃO DE EXERCÍCIOS
# ============================================================

def gerar_exercicios(tema: str, modelo_emb, indices_rag,
                     tipo: str = "misto",
                     quantidade: int = 3) -> str:
    """
    Gera exercícios variados sobre um tema com base nos materiais do RAG.

    Parâmetros:
        tema        — assunto dos exercícios
        modelo_emb  — SentenceTransformer carregado
        indices_rag — IndicesRAG carregado
        tipo        — "multipla_escolha" | "verdadeiro_falso" | "aberta" | "misto"
        quantidade  — número de questões (máximo 5)

    Retorna:
        String formatada com os exercícios prontos para o usuário.
    """
    quantidade = min(quantidade, 5)  # limita a 5 por chamada
    contexto   = _recuperar_contexto(tema, modelo_emb, indices_rag, top_k=5)

    if not contexto:
        return (
            f"❌ Não encontrei material suficiente sobre '{tema}' nos documentos indexados.\n"
            "Tente usar um termo mais próximo do conteúdo das aulas."
        )

    # Monta a instrução de tipo
    instrucoes_tipo = {
        "multipla_escolha": (
            f"Crie {quantidade} questões de múltipla escolha (A, B, C, D). "
            "Para cada questão, indique a alternativa correta ao final."
        ),
        "verdadeiro_falso": (
            f"Crie {quantidade} afirmações de Verdadeiro ou Falso. "
            "Indique a resposta correta e uma breve justificativa ao final de cada uma."
        ),
        "aberta": (
            f"Crie {quantidade} questões dissertativas abertas que exijam explicação conceitual. "
            "Inclua um gabarito resumido ao final de cada questão."
        ),
        "misto": (
            f"Crie {quantidade} exercícios variados: misture múltipla escolha, "
            "verdadeiro/falso e questão aberta. "
            "Indique o tipo de cada questão e o gabarito ao final."
        ),
    }
    instrucao = instrucoes_tipo.get(tipo, instrucoes_tipo["misto"])

    prompt_sistema = (
            "Você é um professor avaliando uma resposta de um aluno. "
            "REGRA 1: Avalie APENAS o que foi pedido. Se a pergunta pede uma fórmula e o aluno deu a fórmula, considere EXCELENTE e sem lacunas. Não exija explicações extras se não foram solicitadas na pergunta. "
            "REGRA 2: O aluno PODE usar formatação LaTeX ou texto livre. NUNCA critique a formatação da resposta do aluno. "
            "REGRA 3 (PARA VOCÊ): Nas SUAS explicações e feedbacks, É PROIBIDO usar LaTeX (como \\[, \\], \\frac, $$). Escreva matemática em texto simples.\n\n"
            "Estruture exatamente assim:\n"
            "✅ Acertos: ...\n"
            "❌ Lacunas: ... (Deixe vazio se a resposta atendeu ao que foi perguntado)\n"
            "💡 Complemento: ... (Adicione curiosidades ou contexto aqui sem penalizar o aluno)\n"
            "⭐ Avaliação: [Excelente / Boa / Parcial / Insuficiente]"
        )
    prompt_usuario = (
        f"Tema: {tema}\n\n"
        f"Contexto dos materiais de aula:\n{contexto}\n\n"
        f"Instrução: {instrucao}"
    )

    exercicios = _chamar_llm(prompt_sistema, prompt_usuario)

    cabecalho = (
        f"📝 *Exercícios — {tema}*\n"
        f"Tipo: {tipo.replace('_', ' ').title()} | Quantidade: {quantidade}\n"
        f"{'─' * 40}\n\n"
    )

    return cabecalho + exercicios