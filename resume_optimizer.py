# import os
# import time
# import csv
# from datetime import datetime
# from transformers import pipeline

# # Load the Hugging Face pipeline with a text-to-text model
# rewriter = pipeline("text2text-generation", model="google/flan-t5-base")
# #     prompt = f"""You are an expert resume writer.
# # Rewrite the following resume section in a {tone} tone.
# # {f"Make it relevant for the job title: {job_title}." if job_title else ""}

# def optimize_resume_section(section_text: str, tone: str = "professional", job_title: str = None) -> str:
#     prompt = f"""You are a career coach. 
# Rewrite the following resume section in a {tone} tone to sound polished and professional. 
# Emphasize relevance for a {job_title if job_title else 'general'} role.

# Resume Section:
# \"\"\"
# {section_text}
# \"\"\"

# Rewritten:"""

#     try:
#         start_time = time.time()
#         response = rewriter(prompt, max_new_tokens=200)
#         end_time = time.time()

#         generated = response[0]['generated_text'].strip()
#         tokens_used = len(generated.split())
#         latency = round(end_time - start_time, 2)

#         log_llm_metrics(
#             prompt, generated, tokens_used, latency,
#             model_name="flan-t5-base", task="Resume Rewriting"
#         )

#         return generated

#     except Exception as e:
#         return f"Error optimizing resume: {e}"
    
# def log_llm_metrics(prompt, output, tokens_used, latency, model_name, task):
#     os.makedirs("logs", exist_ok=True)
#     log_path = "logs/llm_metrics_resume.csv"
#     header = ["Timestamp", "Task", "Model", "Tokens", "Latency(s)", "Prompt", "Output"]

#     row = [
#         datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         task,
#         model_name,
#         tokens_used,
#         latency,
#         prompt.replace("\n", " "),
#         output.replace("\n", " ")
#     ]

#     write_header = not os.path.exists(log_path)

#     with open(log_path, "a", encoding="utf-8", newline="") as f:
#         writer = csv.writer(f)
#         if write_header:
#             writer.writerow(header)
#         writer.writerow(row)






# ===================================
# OpenAPI method
# ===================================
import os
import time
import csv
from datetime import datetime
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- Define logger first ----------
def log_llm_metrics(prompt, output, tokens_used, latency, model_name, task):
    os.makedirs("logs", exist_ok=True)
    log_path = "logs/llm_metrics_resume.csv"
    header = ["Timestamp", "Task", "Model", "Tokens", "Latency(s)", "Prompt", "Output"]

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        task,
        model_name,
        tokens_used,
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

# ---------- Resume Optimizer Function ----------
def optimize_resume_section(section_text: str, tone: str = "professional", job_title: Optional[str] = None) -> str:
    prompt = f"""You are an expert resume writer.
Rewrite the following resume section in a {tone} tone.
{f"Make it relevant for the job title: {job_title}." if job_title else ""}
Keep the response clear and impactful.

Resume Section:
\"\"\"
{section_text}
\"\"\"

Rewritten:"""

    try:
        start_time = time.time()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        end_time = time.time()

        generated = response.choices[0].message.content
        generated = generated.strip() if generated else "[No response generated]"

        tokens_used = len(generated.split())
        latency = round(end_time - start_time, 2)

        log_llm_metrics(
            prompt, generated, tokens_used, latency,
            model_name="gpt-3.5-turbo", task="Resume Rewriting"
        )

        return generated

    except Exception as e:
        return f"!!! Error optimizing resume: {e}"
