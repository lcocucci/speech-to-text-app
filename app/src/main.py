from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from .apis.stt_api import router
    
app = FastAPI()
app.include_router(router, prefix='/api', tags=['stt'])

@app.get('/')
def root():
    with open('app/src/index.html', 'r') as file:
        html_response = file.read()
    return HTMLResponse(content = html_response)