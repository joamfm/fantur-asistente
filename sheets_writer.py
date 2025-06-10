
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Ruta local al archivo JSON de credenciales
CREDENTIALS_FILE = "fantur-462502-a88748375bae.json"

# ID de la planilla de Google Sheets
SPREADSHEET_ID = "1-D8YrT1KxI7F3p9MRP7TS6Xv9OJZD9SJcyUtOCgyQDc"

# Inicializa la conexión a Google Sheets
def connect_to_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    return sheet

# Registra una fila con los datos de la interacción
def registrar_interaccion(user_id, user_message, bot_response, state):
    try:
        sheet = connect_to_sheet()
        timestamp = datetime.now().isoformat()
        row = [timestamp, user_id, user_message, bot_response, state]
        sheet.append_row(row)
        print(f"[Sheets] Interacción registrada para {user_id}")
    except Exception as e:
        print(f"[Sheets] Error al registrar: {e}")
