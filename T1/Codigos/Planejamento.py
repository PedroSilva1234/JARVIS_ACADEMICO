"""
planejamento.py — Módulo 3.4: Planejamento de Estudos do JARVIS Acadêmico
=========================================================================
Combina agenda (Google Calendar), tarefas (JSON local) e materiais (RAG)
para gerar um plano de estudos personalizado e priorizado.

Integração:
  - Importado pelo gerar_respostas.py como ferramenta adicional
  - Registrar a ferramenta 'montar_plano_estudos' no DESCRICAO_FERRAMENTAS
  - Chamar executar_ferramenta() com o nome 'montar_plano_estudos'

Uso no system prompt (adicione à DESCRICAO_FERRAMENTAS):
  10. montar_plano_estudos
     - Uso: quando o usuário pedir um plano de estudos, priorização do dia
       ou estratégia para uma prova.
     - JSON: {"tool": "montar_plano_estudos", "args": {"janela_dias": 7, "foco": "prova de cálculo"}}
     - janela_dias: quantos dias à frente considerar (padrão: 7)
     - foco: tema ou prova específica (opcional, string vazia = geral)
"""

import json
import os
from datetime import date, timedelta

from google_agenda import consultar_agenda_real
from retrieval import buscar_hibrido

ARQUIVO_TAREFAS = "tarefas.json"

# ============================================================
# HELPERS
# ============================================================

def _carregar_tarefas() -> list:
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    try:
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def _dias_ate(prazo_str: str) -> int:
    """Retorna quantos dias faltam até o prazo. Negativo = atrasado."""
    try:
        prazo = date.fromisoformat(prazo_str)
        return (prazo - date.today()).days
    except Exception:
        return 999


def _score_prioridade(tarefa: dict) -> float:
    """
    Calcula um score numérico para ordenar tarefas.
    Quanto menor o score, mais urgente/importante.
      - Prioridade alta   → peso 1
      - Prioridade media  → peso 2
      - Prioridade baixa  → peso 3
      - Dias restantes    → adicionado ao peso (negativo = atrasado, vem primeiro)
    """
    pesos = {"alta": 1, "media": 2, "baixa": 3}
    peso_prio = pesos.get(tarefa.get("prioridade", "baixa"), 3)
    dias = _dias_ate(tarefa.get("prazo", "9999-12-31"))
    return peso_prio * 10 + dias


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def montar_plano_estudos(modelo_emb, indices_rag,
                         janela_dias: int = 7,
                         foco: str = "") -> str:
    """
    Gera um plano de estudos estruturado combinando:
      1. Eventos da agenda nos próximos `janela_dias` dias
      2. Tarefas pendentes ordenadas por urgência/prioridade
      3. Materiais relevantes recuperados via RAG

    Parâmetros:
        modelo_emb  — SentenceTransformer carregado
        indices_rag — IndicesRAG carregado
        janela_dias — janela de dias a considerar (padrão 7)
        foco        — tema/prova específica para busca RAG (opcional)

    Retorna:
        String formatada pronta para ser enviada à LLM como contexto.
    """
    hoje = date.today()
    plano = []
    plano.append(f"=== DADOS COLETADOS PARA PLANEJAMENTO ({hoje.isoformat()}) ===\n")

    # ── 1. AGENDA ─────────────────────────────────────────────
    plano.append("📅 EVENTOS NA AGENDA (próximos dias):")
    eventos_encontrados = False

    for i in range(janela_dias):
        dia = (hoje + timedelta(days=i)).isoformat()
        resultado_agenda = consultar_agenda_real(dia)

        # Filtra respostas vazias
        if "Nenhum evento" not in resultado_agenda:
            plano.append(f"  {resultado_agenda.strip()}")
            eventos_encontrados = True

    if not eventos_encontrados:
        plano.append(f"  Nenhum evento nos próximos {janela_dias} dias.")

    plano.append("")

    # ── 2. TAREFAS ────────────────────────────────────────────
    plano.append("📋 TAREFAS PENDENTES (ordenadas por urgência):")
    tarefas = _carregar_tarefas()
    pendentes = [t for t in tarefas if t.get("status") == "pendente"]

    if pendentes:
        pendentes_ordenadas = sorted(pendentes, key=_score_prioridade)
        for t in pendentes_ordenadas:
            dias_restantes = _dias_ate(t.get("prazo", ""))
            if dias_restantes < 0:
                status_prazo = f"⚠️ ATRASADA há {abs(dias_restantes)} dia(s)"
            elif dias_restantes == 0:
                status_prazo = "🔴 Vence HOJE"
            elif dias_restantes <= 2:
                status_prazo = f"🟠 Vence em {dias_restantes} dia(s)"
            else:
                status_prazo = f"🟢 {dias_restantes} dias restantes"

            plano.append(
                f"  [{t['id']}] {t['titulo']} | "
                f"Prioridade: {t.get('prioridade','?')} | "
                f"Prazo: {t.get('prazo','?')} | {status_prazo}"
            )
    else:
        plano.append("  Nenhuma tarefa pendente encontrada.")

    plano.append("")

    # ── 3. MATERIAIS VIA RAG ──────────────────────────────────
    plano.append("📚 MATERIAIS RELEVANTES (RAG):")

    # Define a query de busca: usa o foco se fornecido, senão busca geral
    query_rag = foco if foco.strip() else "resumo geral dos tópicos principais"

    try:
        resultados = buscar_hibrido(
            query=query_rag,
            modelo=modelo_emb,
            indices=indices_rag,
            top_k=4,
            peso_semantico=0.6
        )

        if resultados:
            for i, r in enumerate(resultados, 1):
                trecho = r['texto'][:300].replace('\n', ' ')
                plano.append(
                    f"  [{i}] Origem: {r['origem']} (score: {r['score_final']})\n"
                    f"       Trecho: {trecho}..."
                )
        else:
            plano.append("  Nenhum material relevante encontrado no RAG.")
    except Exception as e:
        plano.append(f"  Erro ao consultar RAG: {e}")

    plano.append("")
    plano.append("=== FIM DOS DADOS ===")
    plano.append(
        "\nCom base nos dados acima, monte um plano de estudos claro e priorizado. "
        "Considere os prazos das tarefas, os eventos da agenda e os materiais disponíveis. "
        "Organize por dia e indique o que estudar primeiro."
        + (f" Foco especial em: {foco}." if foco.strip() else "")
    )

    return "\n".join(plano)