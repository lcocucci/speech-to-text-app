import whisper
from datetime import datetime

# Desde un archivo de audio
def stt_whisper_audiofile(audiofile: str):
    model = whisper.load_model('base')
    transcription = model.transcribe(audiofile)

    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open(f'app\\src\\samples\\transcriptions\\stt-wl-{now}.txt', 'w') as f:
        f.write(transcription['text'])
        