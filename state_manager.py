
user_states = {}

def get_user_state(user_id):
    return user_states.get(user_id, {"paso": 0, "respuestas": []})

def update_user_state(user_id, state):
    user_states[user_id] = state
