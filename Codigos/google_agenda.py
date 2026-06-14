import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Adicionamos o escopo de TASKS além do CALENDAR
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/tasks'
]
load_dotenv()
def obter_credenciais():
    """Gerencia a autenticação e retorna as credenciais válidas."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.getenv(r'CREDENTIALS_JSON'), SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def autenticar_google():
    """Retorna o serviço do Google Calendar."""
    return build('calendar', 'v3', credentials=obter_credenciais())

def autenticar_tasks():
    """Retorna o serviço do Google Tasks."""
    return build('tasks', 'v1', credentials=obter_credenciais())

# ============================================================
# EVENTOS (GOOGLE CALENDAR)
# ============================================================

def consultar_agenda_real(data_str: str) -> str:
    """Busca eventos na agenda do Google para um dia (YYYY-MM-DD) ou mês completo (YYYY-MM)."""
    try:
        servico = autenticar_google()
        data_str = data_str.strip()
        
        # Detecta se a busca é por mês (YYYY-MM) ou por dia (YYYY-MM-DD)
        if len(data_str) == 7:
            data_inicio = datetime.datetime.strptime(data_str, "%Y-%m")
            # Força o fuso horário local (-04:00) em vez do Zulu ('Z')
            inicio_periodo = f"{data_str}-01T00:00:00-04:00"
            
            if data_inicio.month == 12:
                data_fim = datetime.datetime(data_inicio.year + 1, 1, 1)
            else:
                data_fim = datetime.datetime(data_inicio.year, data_inicio.month + 1, 1)
            fim_periodo = f"{data_fim.strftime('%Y-%m-%d')}T00:00:00-04:00"
            
            print(f"📅 Buscando todos os eventos na nuvem para o mês: {data_str}...")
        else:
            # Comportamento padrão por dia
            data_inicio = datetime.datetime.strptime(data_str, "%Y-%m-%d")
            # Força o fuso horário local (-04:00) 
            inicio_periodo = f"{data_str}T00:00:00-04:00"
            data_fim = data_inicio + datetime.timedelta(days=1)
            fim_periodo = f"{data_fim.strftime('%Y-%m-%d')}T00:00:00-04:00"
            
            print(f"📅 Buscando eventos na nuvem para o dia: {data_str}...")
        
        eventos_result = servico.events().list(
            calendarId='primary', 
            timeMin=inicio_periodo,
            timeMax=fim_periodo,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        eventos = eventos_result.get('items', [])

        if not eventos:
            return f"Nenhum evento encontrado para o período [{data_str}]."

        resultado = f"Eventos encontrados no Google Calendar para [{data_str}]:\n"
        for evento in eventos:
            inicio = evento['start'].get('dateTime', evento['start'].get('date'))
            dia_mes = f"{inicio[8:10]}/{inicio[5:7]}"
            horario = inicio[11:16] if 'T' in inicio else 'O dia todo'
            resultado += f"  • [{dia_mes}] às {horario} - {evento['summary']}\n"
            
        return resultado

    except Exception as e:
        return f"Erro ao acessar a agenda do Google: {type(e).__name__}: {e}"
    
def buscar_evento_por_titulo(titulo: str) -> str:
    """Busca eventos na agenda pelo título e retorna os detalhes para confirmação."""
    try:
        servico = autenticar_google()
        # O parâmetro 'q' faz uma busca textual em todos os eventos
        eventos_result = servico.events().list(
            calendarId='primary', q=titulo, singleEvents=True, orderBy='startTime'
        ).execute()
        
        eventos = eventos_result.get('items', [])

        if not eventos:
            return f"Nenhum evento com o termo '{titulo}' foi encontrado na agenda."

        resultado = ""
        for ev in eventos:
            inicio = ev['start'].get('dateTime', ev['start'].get('date'))
            # Extraindo a data de forma amigável para a IA ler
            data_formatada = inicio[:10].split('-')
            data_br = f"{data_formatada[2]}/{data_formatada[1]}/{data_formatada[0]}"
            horario = inicio[11:16] if 'T' in inicio else "o dia todo"
            
            resultado += f"- Evento: '{ev['summary']}' | Data: {data_br} ({horario})\n"

        return resultado.strip()
    except Exception as e:
        return f"Erro ao buscar o evento: {e}"
    
def criar_evento_real(titulo: str, data_str: str, descricao: str = "", hora_inicio: str = None, hora_fim: str = None) -> dict:
    try:
        servico = autenticar_google()
        evento = {
            'summary': titulo,
            'description': descricao,
        }
        # Se recebeu os horários, cria o evento de "timebox" com o fuso local (Campo Grande)
        if hora_inicio and hora_fim:
            evento['start'] = {
                'dateTime': f"{data_str}T{hora_inicio}:00",
                'timeZone': 'America/Campo_Grande'
            }
            evento['end'] = {
                'dateTime': f"{data_str}T{hora_fim}:00",
                'timeZone': 'America/Campo_Grande'
            }
        else:
            # Evento de dia inteiro (padrão antigo)
            evento['start'] = {'date': data_str}
            evento['end'] = {'date': data_str}
            
        evento_criado = servico.events().insert(calendarId='primary', body=evento).execute()
        return {"sucesso": True, "id": evento_criado.get('id')}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}


def deletar_evento_real(titulo: str) -> str:
    """Busca um evento pelo título e remove da Agenda do Google."""
    try:
        servico = autenticar_google()
        # Busca eventos contendo o termo no título
        eventos_result = servico.events().list(calendarId='primary', q=titulo).execute()
        eventos = eventos_result.get('items', [])
        
        if not eventos:
            return f"Nenhum evento contendo '{titulo}' foi localizado na agenda."
            
        deletados = 0
        for ev in eventos:
            if titulo.lower() in ev.get('summary', '').lower():
                servico.events().delete(calendarId='primary', eventId=ev['id']).execute()
                deletados += 1
                
        return f"✅ Sucesso! {deletados} evento(s) com o termo '{titulo}' foram removidos da nuvem."
    except Exception as e:
        return f"Erro ao remover evento da agenda: {e}"

def consultar_proximos_eventos(dias_frente: int = 7) -> str:
    """Busca eventos na agenda a partir de hoje até 7 dias para frente."""
    try:
        servico = autenticar_google()
        
        # Pega o momento atual (timeMin)
        agora = datetime.datetime.utcnow()
        inicio_periodo = agora.isoformat() + 'Z'
        
        # Calcula o teto (timeMax)
        fim_periodo = (agora + datetime.timedelta(days=dias_frente)).isoformat() + 'Z'
        
        eventos_result = servico.events().list(
            calendarId='primary', 
            timeMin=inicio_periodo,
            timeMax=fim_periodo,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        eventos = eventos_result.get('items', [])

        if not eventos:
            return f"A agenda está livre! Nenhum evento encontrado para os próximos {dias_frente} dias."

        resultado = f"Próximos compromissos (janela de {dias_frente} dias):\n"
        for evento in eventos:
            inicio = evento['start'].get('dateTime', evento['start'].get('date'))
            dia_mes = f"{inicio[8:10]}/{inicio[5:7]}"
            horario = inicio[11:16] if 'T' in inicio else 'O dia todo'
            resultado += f"  • [{dia_mes}] às {horario} - {evento['summary']}\n"
            
        return resultado
    except Exception as e:
        return f"Erro ao acessar os próximos eventos: {e}"
# ============================================================
# TAREFAS (GOOGLE TASKS)
# ============================================================

def criar_task_real(titulo: str, prazo_str: str, descricao: str = "") -> dict:
    """Cria uma tarefa real no Google Tasks."""
    try:
        servico = autenticar_tasks()
        # O Google Tasks exige formato de data RFC3339 (Ex: 2026-07-12T00:00:00.000Z)
        data_rfc = f"{prazo_str}T00:00:00.000Z"
        
        task_body = {
            'title': titulo,
            'notes': descricao,
            'due': data_rfc
        }
        # Insere na lista padrão de tarefas do usuário (@default)
        task_criada = servico.tasks().insert(tasklist='@default', body=task_body).execute()
        return {"sucesso": True, "id": task_criada.get('id')}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

def concluir_task_real(task_id: str) -> str:
    """Marca uma tarefa como concluída no Google Tasks."""
    try:
        servico = autenticar_tasks()
        task = servico.tasks().get(tasklist='@default', task=task_id).execute()
        task['status'] = 'completed'
        servico.tasks().update(tasklist='@default', task=task_id, body=task).execute()
        return "Status atualizado com sucesso no Google Tasks!"
    except Exception as e:
        return f"Erro ao concluir no Google Tasks: {e}"

def deletar_task_real(task_id: str) -> str:
    """Deleta uma tarefa permanentemente do Google Tasks."""
    try:
        servico = autenticar_tasks()
        servico.tasks().delete(tasklist='@default', task=task_id).execute()
        return "Removida com sucesso do Google Tasks!"
    except Exception as e:
        return f"Erro ao deletar do Google Tasks: {e}"
    
if __name__ == '__main__':
    hoje = datetime.date.today().isoformat()
    print(consultar_agenda_real(hoje))