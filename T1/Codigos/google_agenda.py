import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permissão apenas para LER a agenda (segurança em primeiro lugar)
SCOPES = ['https://www.googleapis.com/auth/calendar']

def autenticar_google():
    """Autentica o usuário e retorna o serviço da API do Calendar."""
    creds = None
    
    # O arquivo token.json armazena os tokens de acesso do usuário.
    # Ele é criado automaticamente após o primeiro login bem-sucedido.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # Se não houver credenciais válidas, exige o login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("🔐 Abrindo navegador para autenticação do Google...")
            flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\ppedr\\Desktop\\2025\\UFMS\\IA\\T1\\Codigos\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Salva as credenciais para a próxima execução
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def criar_evento_real(titulo: str, data_str: str, descricao: str = "") -> str:
    """Cria um evento de dia inteiro na agenda do Google."""
    try:
        servico = autenticar_google()
        
        evento = {
            'summary': titulo,
            'description': descricao,
            'start': {
                'date': data_str,  # Formato YYYY-MM-DD para evento de dia inteiro
            },
            'end': {
                'date': data_str,
            },
            'reminders': {
                'useDefault': True
            }
        }
        
        evento_criado = servico.events().insert(calendarId='primary', body=evento).execute()
        return f"Sucesso! Link do evento: {evento_criado.get('htmlLink')}"
        
    except Exception as e:
        return f"Erro ao criar evento no Google Calendar: {e}"
    
def consultar_agenda_real(data_str: str) -> str:
    """Busca eventos na agenda do Google para a data especificada (Formato: YYYY-MM-DD)."""
    try:
        servico = autenticar_google()
        
        # Converte a string de data para o formato de tempo do Google (RFC3339)
        inicio_dia = datetime.datetime.strptime(data_str, "%Y-%m-%d").isoformat() + 'Z'
        fim_dia = (datetime.datetime.strptime(data_str, "%Y-%m-%d") + datetime.timedelta(days=1)).isoformat() + 'Z'

        print(f"📅 Buscando eventos na nuvem para {data_str}...")
        
        eventos_result = servico.events().list(
            calendarId='primary', 
            timeMin=inicio_dia,
            timeMax=fim_dia,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        eventos = eventos_result.get('items', [])

        if not eventos:
            return f"Nenhum evento encontrado para a data {data_str}."

        resultado = f"Eventos encontrados no Google Calendar em {data_str}:\n"
        for evento in eventos:
            inicio = evento['start'].get('dateTime', evento['start'].get('date'))
            # Limpa o horário para ficar mais legível, se houver
            horario = inicio[11:16] if 'T' in inicio else 'O dia todo'
            resultado += f"  • {horario} - {evento['summary']}\n"
            
        return resultado

    except Exception as e:
        return f"Erro ao acessar a agenda do Google: {e}"

# =======================================================
# Teste Rápido (Só roda se você executar este arquivo diretamente)
# =======================================================
if __name__ == '__main__':
    hoje = datetime.date.today().isoformat()
    print(consultar_agenda_real(hoje))