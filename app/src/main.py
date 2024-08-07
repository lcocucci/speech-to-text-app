from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from .apis.stt_api import router
from datetime import datetime
from .services.whisper_streaming_service import stt_whisper_streaming_af
    
app = FastAPI()
app.include_router(router, prefix='/api', tags=['stt'])

# Renderizamos el archivo index.html en la raíz de la aplicación cliente
@app.get('/')
def root():
    with open('app/src/index.html', 'r') as file:
        html_response = file.read()
    return HTMLResponse(content = html_response)

# Realizamos la conexión a websockets
@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
    await ws.accept() # Aceptamos la conexión de websockets
    while True:
        data = await ws.receive_bytes() # Quedamos a la espera de recibir datos del cliente
        now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_path = f'app/src/samples/audio/stt-staf-{now}.wav' # Guardamos la ubicación exacta del archivo
        with open(file_path, 'wb') as f:
            f.write(data)
        print('Archivo de audio recibido y guardado')
        await ws.send_text('Archivo de audio guardado')
        stt_whisper_streaming_af(file_path)
        print('Transcripción Completada :)')
        