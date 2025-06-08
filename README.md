
# Asistente Fantur (Versión Railway)

Este es un servidor Flask que actúa como webhook para un asistente conversacional de WhatsApp que ayuda a crear una web paso a paso.

## Estructura
- `main.py`: servidor principal
- `flow.py`: lógica del flujo conversacional
- `state_manager.py`: control de estado de usuarios

## Cómo usar en Railway
1. Subí este proyecto a un repositorio de GitHub
2. Conectalo a Railway (Deploy from GitHub)
3. Railway detectará `main.py` y `requirements.txt` automáticamente
4. Seteá la ruta `/webhook` como endpoint para recibir mensajes

