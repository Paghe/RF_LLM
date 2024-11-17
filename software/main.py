
from receiver import receiver
from transmitter import transmitter
import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    if result is None:
        raise ValueError("AUDIO_FILE_PATH environment variable is not set")
    print(result["text"])

def main():
    # transmitter()
    # receiver()
    audio_path = "/app/audio1.wav"
    transcribe_audio(audio_path)

if __name__ == "__main__":
    main()