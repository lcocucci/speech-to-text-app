FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Descargamos y guardamos el modelo Whisper durante la construcción de la imagen
RUN python -c "from faster_whisper import WhisperModel; model = WhisperModel('small', device='cpu', compute_type='int8')"

COPY . /app/

EXPOSE 8000

CMD [ "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]