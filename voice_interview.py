import whisper
import tempfile
import os
from transformers import pipeline
from datetime import datetime

# Load models
model = whisper.load_model("base")
feedback_model = pipeline("text2text-generation", model="google/flan-t5-base")

LOG_FILE = "logs/interview_log.txt"

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
        feedback = response[0]['generated_text'].strip()
        log_interview_response(transcript, feedback)
        return feedback
    except Exception as e:
        return f"Error generating feedback: {e}"

def log_interview_response(transcript: str, feedback: str):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n---\n {timestamp}\n")
        f.write(f"Transcript: {transcript}\n")
        f.write(f"Feedback: {feedback}\n")
