from pydantic import BaseModel

class STTAudioFile(BaseModel):
    audio_file: str
    method: str