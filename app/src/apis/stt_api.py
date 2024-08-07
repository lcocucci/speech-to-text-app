from fastapi import APIRouter, HTTPException
from ..models.item import STTAudioFile, STTStreamingChunks
from ..services.whisper_audiofile_service import stt_whisper_audiofile
from ..services.whisper_streaming_service import stt_whisper_streaming

router = APIRouter()

@router.post('/stt-audio-file')
def stt_audio_file(model_request: STTAudioFile):
    if model_request.method == 'af-whisper':
        return stt_whisper_audiofile(model_request.audio_file)
    elif model_request.method == 'staf-whisper':
        return stt_whisper_streaming()
    else:
        raise HTTPException(status_code=404,detail='Método Incorrecto')

@router.post('/stt-streaming-chunks')
def stt_streaming(model_request: STTStreamingChunks):
        return stt_whisper_streaming()