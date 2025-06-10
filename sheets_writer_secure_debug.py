import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import json

SPREADSHEET_ID = "1-D8YrT1KxI7F3p9MRP7TS6Xv9OJZD9SJcyUtOCgyQDc"

def connect_to_sheet():
    print("[DEBUG] Leyendo GOOGLE_SHEETS_CREDS...")
    raw_creds = os.environ.get("GOOGLE_SHEETS_CREDS", "NO DEFINIDA")
    print("[DEBUG] Resultado:", raw_creds[:100] + "..." if raw_creds != "NO DEFINIDA" else raw_creds)

    if raw_creds == "NO DEFINIDA":
        raise Exception("Variable de entorno GOOGLE_SHEETS_CREDS no está definida")

    creds_info = json.loads(raw_creds)
    creds = Credentials.from_service_account_info(creds_info, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    return sheet

def registrar_interaccion(user_id, user_message, bot_response, state):
    try:
        sheet = connect_to_sheet()

        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # timestamp
            user_id,
            user_message,
            bot_response,
        ]

        # Aplanar y convertir el diccionario del estado a texto para evitar errores
        for key in ["paso", "respuestas"]:
            valor = state.get(key, "")
            if isinstance(valor, (dict, list)):
                row.append(json.dumps(valor, ensure_ascii=False))
            else:
                row.append(str(valor))

        print("[DEBUG] Fila generada:", row)
        sheet.append_row(row)
        print("[Sheets] Registro exitoso en la hoja de cálculo.")

    except Exception as e:
        print("[Sheets] Error al registrar:", e)

