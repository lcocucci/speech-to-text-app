from datetime import datetime
from time import time
# import warnings
from faster_whisper import WhisperModel

# Desde un archivo de audio
def stt_whisper_audiofile(audiofile: str):
    model = WhisperModel("small", device="cpu", compute_type="int8")

    print('Inicio de Transcripción')
    start_time = time()
    
    segments, info = model.transcribe(audiofile, language="es")
    
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "
        
    end_time = time()
    tr_duration = end_time - start_time
    print(f'Tiempo de Transcripción: {tr_duration}')

    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open(f'app\\src\\samples\\transcriptions\\af-{now}.txt', 'w', encoding='utf-8') as f:
        f.write(transcription)

    print(f"Transcripción Completada :)")