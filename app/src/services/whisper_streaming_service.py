import whisper
import pyaudio
import numpy as np
from threading import Thread
from datetime import datetime
from time import time
import warnings

warnings.filterwarnings("ignore")
now = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

def stt_whisper_streaming():
    # Inicializar el modelo de Whisper
    model = whisper.load_model("base")

    # Configuración de PyAudio
    CHUNK = 1024  # Tamaño del fragmento
    FORMAT = pyaudio.paInt16  # Formato de audio
    CHANNELS = 1  # Canal de audio
    RATE = 16000  # Frecuencia de muestreo (16kHz)

    p = pyaudio.PyAudio()

    # Inicializar el flujo de audio
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening...")

    def transcribe_audio(frames):
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / 32768.0
        result = model.transcribe(audio_data, fp16=False)
        print(result['text'])

    seconds_per_chunk = CHUNK / RATE
    
    def transcribe():
        frames = []
        while True:
            # Capturar el audio
            data = stream.read(CHUNK)
            frames.append(data)

            # Si se ha capturado un fragmento de 5 segundos, transcribir
            if len(frames) >= int(5 / seconds_per_chunk):
                # Procesar el audio en un hilo separado para evitar bloqueos
                t = Thread(target=transcribe_audio, args=(frames,))
                t.start()
                frames = []

    try:
        transcribe()
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        
# Transcripción en Streaming que se procesa como un archivo de audio
def stt_whisper_streaming_af(audiofile: str):
    model = whisper.load_model('small')
    print('Inicio de Transcripción')
    start_time = time()
    transcription = model.transcribe(audiofile, language='es')
    end_time = time()
    tr_duration = end_time - start_time
    print(f'Tiempo de Transcripción: {tr_duration}')
    
    with open(f'app\\src\\samples\\transcriptions\\stt-staf-{now}.txt', 'w', encoding='utf-8') as f:
        f.write(transcription['text'])
    
# Transcripción en Streaming que va procesando pequeños fragmentos en tiempo real
def stt_whisper_streaming_chunks():
    ...