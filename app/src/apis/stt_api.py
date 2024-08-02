from fastapi import APIRouter, HTTPException
from models.item import STTAudioFile
from services.whisper_local_service import stt_whisper_local
# from services.whisper_api_service import stt_whisper_api

router = APIRouter()

@router.post('/stt-audio-file')
def stt_audio_file(model_request: STTAudioFile):
    if model_request.method == 'local-whisper':
        return stt_whisper_local(model_request.audio_file)
    # elif model_request.method == 'api-whisper':
    #     return await stt_whisper_api(model_request.audio_file)
    else:
        raise HTTPException(status_code=404,detail='Método Incorrecto')

@router.post('/stt-streaming')
def stt_streaming():
    ...