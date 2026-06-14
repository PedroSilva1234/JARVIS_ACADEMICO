import json
import os

ARQUIVO_DADOS = "dados_pessoais.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return {"agenda": {}, "tarefas": []}
    with open(ARQUIVO_DADOS,'r', encoding='utf-8') as f:
        return json.load(f)
    

def salvar_dado(dados):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados,f,ensure_ascii=False, indent=4)



def consultar_agenda(data:str) ->str:
    dados = carregar_dados()
    eventos = dados["agenda"].get(data, [])
    if not eventos:
        return f"Nenhum envento encontrado para a data {data}"
    
    return f"Eventos em {data}: \n"+ "\n".join(f" .  {e}" for e in eventos)

def adicionar_eventos(data:str, evento:str) -> str:

    dados = carregar_dados
    if data not in dados ["agenda"]:
        dados["agendas"][data] = []
    dados["agenda"][data].append(evento)
    salvar_dado(dados)
    return f"Evento '{evento}' adicionado na agenda para o dia {data}."


def listar_tarefas(status: str) -> str:
    dados = carregar_dados()
    filtradas = [t for t in dados["tarefas"] if t["status"] == status]
    if not filtradas:
        return f"Nenhuma tarefa com status '{status}'."
    linhas = [f"  [{t['id']}] {t['titulo']} | Prazo: {t['prazo']} | Prioridade: {t['prioridade']}" for t in filtradas]
    return f"Tarefas {status}s:\n" + "\n".join(linhas)

def adicionar_tarefa(titulo: str, prazo: str, prioridade: str) -> str:
    dados = carregar_dados()
    # Acha o último ID usado para não repetir
    novo_id = max([t["id"] for t in dados["tarefas"]], default=0) + 1
    
    dados["tarefas"].append({
        "id": novo_id, "titulo": titulo, "prazo": prazo,
        "prioridade": prioridade, "status": "pendente"
    })
    salvar_dado(dados)
    return f"✅ Tarefa '{titulo}' adicionada com ID {novo_id} (Prazo: {prazo})."

def concluir_tarefa(id_tarefa: int) -> str:
    dados = carregar_dados()
    for t in dados["tarefas"]:
        if t["id"] == id_tarefa:
            t["status"] = "concluida"
            salvar_dado(dados)
            return f"✅ Tarefa '{t['titulo']}' finalizada com sucesso!"
    return f"❌ Tarefa com ID {id_tarefa} não encontrada no sistema."