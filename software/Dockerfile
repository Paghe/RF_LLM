FROM python:3.9

RUN apt-get update && apt-get install -y \
    libatlas-base-dev \
    portaudio19-dev \
    ffmpeg

RUN pip install --no-cache-dir torch torchvision torchaudio
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
COPY start.sh /app/

RUN pip install --no-cache-dir -r requirements.txt
COPY  . /app

CMD ["./start.sh"]
