
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
    user_id = data.get("user_id")
    user_message = data.get("message")

    if not user_id or not user_message:
        return jsonify({"error": "Faltan datos"}), 400

    state = get_user_state(user_id)
    next_message, updated_state = get_next_message(state, user_message)
    update_user_state(user_id, updated_state)

    return jsonify({"reply": next_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
