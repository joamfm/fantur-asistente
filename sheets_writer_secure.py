
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import json

# ID de la planilla de Google Sheets
SPREADSHEET_ID = "1-D8YrT1KxI7F3p9MRP7TS6Xv9OJZD9SJcyUtOCgyQDc"

# Inicializa la conexión a Google Sheets usando una variable de entorno
def connect_to_sheet():
    creds_info = json.loads(os.environ["GOOGLE_SHEETS_CREDS"])
    creds = Credentials.from_service_account_info(creds_info, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
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
