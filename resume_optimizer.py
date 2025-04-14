from transformers import pipeline

# Load the Hugging Face pipeline with a text-to-text model
rewriter = pipeline("text2text-generation", model="google/flan-t5-base")

def optimize_resume_section(section_text: str, tone: str = "professional", job_title: str = None) -> str:
    prompt = f"""Rewrite the following resume section in a {tone} tone.
    {f"Make it suitable for the job title: {job_title}." if job_title else ""}
    Text: {section_text}"""

    try:
        output = rewriter(prompt, max_new_tokens=200)
        return output[0]['generated_text'].strip()
    except Exception as e:
        return f"!! Error optimizing resume: {e}"





# ===================================
# OpenAPI method
# ===================================
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load .env file
# load_dotenv()

# # Initialize OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def optimize_resume_section(section_text: str, tone: str = "professional", job_title: str = None) -> str:
#     prompt = f"""You are an expert resume writer.
# Rewrite the following resume section in a {tone} tone.
# {f"Make it relevant for the job title: {job_title}." if job_title else ""}
# Keep the response clear and impactful.

# Resume Section:
# \"\"\"
# {section_text}
# \"\"\"

# Rewritten:
# """

#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             max_tokens=300
#         )
#         return response.choices[0].message.content.strip()

#     except Exception as e:
#         return f"!!! Error optimizing resume: {e}"
