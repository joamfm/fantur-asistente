
# Diccionario con las preguntas del asistente por pasos
flow = [
    "¡Hola! Soy el Asistente Fantur 🤖\n\n¿Querés armar tu web desde cero? Respondé con: si",
    "📍 Bloque 1 - ¿Cómo te gustaría que te identifiquen? (Título breve - máx. 45 caracteres)",
    "📝 Bajada aclaratoria (máx. 80 caracteres)",
    "📸 ¿Qué imagen o idea visual te imaginás?",
    "🔘 ¿Qué botón te gustaría mostrar?",
    "📍 Bloque 2 - ¿Quién sos? (Título máx. 45 caracteres)",
    "📝 Bajada de la sección quiénes somos",
    "📸 Imagen o visual que represente al equipo",
    "🔘 ¿Qué acción o botón querés acá?",
    "📍 Bloque 3 - ¿Qué te hace diferente? (Título máx. 45 caracteres)",
    "📝 Bajada de tu propuesta de valor",
    "📸 Imagen o concepto visual de tu diferencial",
    "🔘 Botón para esta sección",
    "📍 Bloque 4 - ¿Querés ofrecer vuelos? (Título máx. 45 caracteres)",
    "📝 Bajada explicando cómo ofrecés vuelos",
    "📸 Imagen relacionada con vuelos",
    "🔘 Acción o botón en esta sección",
    "🎉 ¡Gracias! En breve alguien de nuestro equipo se contactará con vos."
]

def get_next_message(state, user_message):
    paso = state.get("paso", 0)
    respuestas = state.get("respuestas", [])

    if paso == 0 and user_message.strip().lower() != "si":
        return flow[0], state  # Sigue pidiendo confirmación

    # Guardar respuesta anterior (si no es el primer mensaje)
    if paso > 0:
        respuestas.append(user_message.strip())

    paso += 1
    if paso >= len(flow):
        paso = len(flow) - 1  # Evita desbordes

    new_state = {"paso": paso, "respuestas": respuestas}
    return flow[paso], new_state
