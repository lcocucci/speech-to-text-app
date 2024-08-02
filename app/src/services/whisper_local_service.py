import whisper
from datetime import datetime

now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

def stt_whisper_local(audiofile: str):
    model = whisper.load_model('base')
    transcription = model.transcribe(audiofile)

    with open(f'samples\\transcriptions\\stt-wl-{now}.txt', 'w') as f:
        f.write(transcription['text'])