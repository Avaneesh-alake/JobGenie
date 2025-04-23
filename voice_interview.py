import whisper
import tempfile
import os
from transformers import pipeline
from datetime import datetime
import time
import csv
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
        start_time = time.time()
        response = feedback_model(prompt, max_new_tokens=100)
        end_time = time.time()

        feedback = response[0]['generated_text'].strip()
        latency = round(end_time - start_time, 2)
        tokens_used = len(feedback.split())

        # Log to file
        log_voice_metrics(
            prompt=transcript,
            output=feedback,
            tokens=tokens_used,
            latency=latency,
            model_name="flan-t5-base",
            task="Voice Feedback"
        )

        log_interview_response(transcript, feedback)  # keep this for content logging
        return feedback

    except Exception as e:
        return f"Error generating feedback: {e}"


def log_voice_metrics(prompt, output, tokens, latency, model_name, task):
    os.makedirs("logs", exist_ok=True)
    log_path = "logs/llm_metrics_voice.csv"
    header = ["Timestamp", "Task", "Model", "Tokens", "Latency(s)", "Prompt", "Output"]

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        task,
        model_name,
        tokens,
        latency,
        prompt.replace("\n", " "),
        output.replace("\n", " ")
    ]

    write_header = not os.path.exists(log_path)

    with open(log_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow(row)


def log_interview_response(transcript: str, feedback: str):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n---\n {timestamp}\n")
        f.write(f"Transcript: {transcript}\n")
        f.write(f"Feedback: {feedback}\n")
