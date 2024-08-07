import whisper
from datetime import datetime

now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

# Desde un archivo de audio
def stt_whisper_audiofile(audiofile: str):
    model = whisper.load_model('base')
    transcription = model.transcribe(audiofile)

    with open(f'app\\src\\samples\\transcriptions\\stt-wl-{now}.txt', 'w') as f:
        f.write(transcription['text'])
        