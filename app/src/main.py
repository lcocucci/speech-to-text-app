from fastapi import FastAPI
from apis.stt_api import router
    
app = FastAPI()
app.include_router(router, prefix='/api', tags=['stt'])

@app.get('/')
def root():
    return {'msg': 'Welcome to FastAPI :)'}