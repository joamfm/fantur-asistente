from whatsapp_sender import send_whatsapp_message
from flask import Flask, request, jsonify
from flow import get_next_message
from state_manager import get_user_state, update_user_state

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Asistente Fantur está activo"
@app.route("/webhook", methods=["GET"])
def verify():
    verify_token = "fantur2025"
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        return challenge, 200
    else:
        return "Unauthorized", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("[Webhook] Payload recibido:")
    print(data)

    try:
        # Estructura real desde WhatsApp (Meta)
        entry = data["entry"][0]
        change = entry["changes"][0]
        message_data = change["value"]["messages"][0]

        user_id = message_data["from"]
        user_message = message_data["text"]["body"]
    except Exception as e:
        print("[Webhook] Error al procesar:", e)
        return jsonify({"error": "Estructura no reconocida", "detalles": str(e)}), 400

    # Usamos el flujo de asistente
    state = get_user_state(user_id)
    next_message, updated_state = get_next_message(state, user_message)
    update_user_state(user_id, updated_state)
    send_whatsapp_message(user_id, next_message)

    # WhatsApp Cloud API requiere responder con status 200 sin datos
    return jsonify({"reply": next_message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
