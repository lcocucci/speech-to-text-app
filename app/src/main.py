import whisper

model = whisper.load_model('base')
transcription = model.transcribe(r'app\src\samples\audio\ElevenLabs_Valeria_test.mp3')

with open(r'app\src\samples\transcriptions\transcription.txt', 'w') as f:
    f.write(transcription['text'])