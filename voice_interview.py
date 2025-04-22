
import whisper
import tempfile
import os

# Load Whisper model once
model = whisper.load_model("base")  # Can be tiny/base/small/medium/large

def transcribe_audio_file(audio_file_path: str) -> str:
    try:
        result = model.transcribe(audio_file_path)
        return result["text"]
    except Exception as e:
        return f"!! Error transcribing audio: {e}"
