
import requests

ACCESS_TOKEN = "EAAUYNX1D8n4BOw2ZCpXISkbHN5YlZARZCFMpHmTMZBRyrx6DXcTbvrgs4g6GJHtt8frI3ZCh0Tdyg8wqdhHtcltdgufq3TGqoDvj3l6KwRTfwk9s10BnGyHF8PxpTwlIFLPm4GYAuM6ZB9ExMmsXjNNYVmz8tQwLX3lYhBFdznPg3nVD2j0rOAxESoqMsOZBcGrqQZDZD"
PHONE_NUMBER_ID = "598116436728931"
GRAPH_URL = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

def send_whatsapp_message(to, message):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": message
        }
    }

    response = requests.post(GRAPH_URL, headers=headers, json=data)
    try:
        response.raise_for_status()
        print("[WhatsApp] Mensaje enviado correctamente:", response.json())
    except requests.exceptions.HTTPError as err:
        print("[WhatsApp] Error al enviar mensaje:", err)
        print("Detalles:", response.text)
