
import requests

ACCESS_TOKEN = "EAAUYNX1D8n4BO1kclCazFYg1FRclbYlhwlodamS8I8hAzyY9JJZApvFf5wXV9WTyP2KSplZAcRn08UgiRfq93Xz3Wo5OUf2R47ZCmtrslhi5d9010j0FkDEsjUl2sRtrykwD5qb19opyNYMwf329LvH0BxfuLyjpLUG9A3TCPUE3i1BuYZC89skAmcH1vDB3VNcrCSxc7fvsZBsEqx8nqVVj35vMBtnJ2R4P4pQvetnKkyVCDyAZDZD"
PHONE_NUMBER_ID = "689360227592552"
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
