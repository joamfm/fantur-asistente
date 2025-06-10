
def registrar_interaccion(user_id, user_message, bot_response, state):
    try:
        sheet = connect_to_sheet()

        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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

        sheet.append_row(row)
        print("[Sheets] Registro exitoso en la hoja de cálculo.")

    except Exception as e:
        print("[Sheets] Error al registrar:", e)
