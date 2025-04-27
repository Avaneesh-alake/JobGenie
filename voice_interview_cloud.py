import os
from datetime import datetime
import csv

LOG_FILE = "logs/interview_log.txt"

def transcribe_audio_file(audio_file_path: str) -> str:
    # Mock transcription for cloud version
    try:
        return "Transcription feature disabled in cloud version to save memory."
    except Exception as e:
        return f"Error transcribing audio: {e}"

def analyze_speech_feedback(transcript: str) -> str:
    try:
        if len(transcript.strip()) < 20:
            feedback = "Your answer is quite short. Try elaborating your response with more details."
        else:
            feedback = "Good response length! Focus on speaking clearly and confidently."
        
        # Log feedback
        log_voice_metrics(
            prompt=transcript,
            output=feedback,
            tokens=len(feedback.split()),
            latency=0.5,  # Dummy latency
            model_name="mock-feedback-generator",
            task="Voice Feedback"
        )
        
        log_interview_response(transcript, feedback)
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
