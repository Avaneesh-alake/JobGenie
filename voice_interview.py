
import whisper
import tempfile
from transformers import pipeline

# Load Whisper model
model = whisper.load_model("base")

# Load feedback model
feedback_model = pipeline("text2text-generation", model="google/flan-t5-base")

def transcribe_audio_file(audio_file_path: str) -> str:
    try:
        result = model.transcribe(audio_file_path)
        return result["text"]
    except Exception as e:
        return f"Error transcribing audio: {e}"

def analyze_speech_feedback(transcript: str) -> str:
    prompt = f"Give brief feedback on this interview answer: '{transcript}'"
    try:
        response = feedback_model(prompt, max_new_tokens=100)
        return response[0]['generated_text'].strip()
    except Exception as e:
        return f"Error generating feedback: {e}"
