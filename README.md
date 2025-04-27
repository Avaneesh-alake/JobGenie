# 💼 JobGenie: AI-Powered Career Assistant
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gradio](https://img.shields.io/badge/Gradio-4.8-orange)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
[![Deployment Status](https://img.shields.io/badge/Deployed%20on-Render-brightgreen)](https://jobgenie-rega.onrender.com)

**JobGenie** is a cloud-native, API-driven AI application that helps job seekers:
- Rewrite resume sections with AI-generated suggestions.
- Analyze job descriptions and match relevant skills.
- Practice voice-based mock interviews with instant feedback.
- Log LLM metrics for monitoring and optimization.

> Developed as part of the **API-Driven Cloud Native Solutions** course at **BITS Pilani**.

---

## Features

### ✍️ Resume Rewriter
- Rewrites poorly written or unstructured resume sections.
- Uses **OpenAI GPT-3.5 Turbo** for professional, confident, or concise tone transformations.
- Accepts optional job titles for context-aware rewriting.

### 📝 Job Description Analyzer
- **Dual skill extraction**:
  - Method 1: Keyword-based (KeyBERT)
  - Method 2: Fine-tuned T5 Model (Hugging Face Transformers)
- Computes **Job Fit Score** by comparing resume vs extracted JD skills.

### 🎤 Voice Interview Assistant
- Uses microphone input to record user response.
- Converts speech to text using Whisper.
- Provides instant **AI-powered feedback** on the spoken response.

### 📊 LLMOps Metrics Dashboard *(Internal Logging)*
- Logs:
  - Prompt
  - Model used
  - Tokens used
  - Response time
  - Output
  - Task type
  - Timestamp

---

## Tech Stack

| Category     | Tools Used |
|--------------|------------|
| Language     | Python 3.10+ |
| Frontend     | Gradio |
| LLMs         | OpenAI GPT-3.5, Hugging Face Flan-T5 |
| Speech-to-Text | OpenAI Whisper |
| Keyword Extraction | KeyBERT |
| Model Training | Hugging Face Transformers, Datasets |
| Logging       | CSV-based custom logger |
| Deployment Ready | Docker + AWS (EC2/S3/Lambda optional as of now) |

---
## Setup Instructions (Local)
---
### 1. Clone the Repo
```bash
git clone https://github.com/Avaneesh-alake/JobGenie.git
cd JobGenie

### 2. Create and Activate Virtual Environment
python -m venv jobgenie-env
jobgenie-env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add Environment Variables
Create a .env file in the root directory:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx

### Run the App
python app.py
The Gradio UI will launch in your browser.
---
### 📁 Directory Structure
JobGenie/
├── app.py
├── resume_optimizer.py
├── job_description_analyzer.py
├── voice_interview.py
├── train_jd_skill_extractor.py
├── predict_skills.py
├── datasets/
│   └── jd_to_skills.csv
├── models/
│   └── jd_skill_extractor/
│       └── final_model/
├── logs/
│   └── llm_metrics_resume.csv
├── requirements.txt
└── .env
---
### 📌 Notes
Fine-tuned Flan-T5 model trained on 80+ JD → Skills examples.
OpenAI used for real-time resume rewriting for high-quality outputs.
All components modular and ready for integration into a production pipeline.
---
###📜 License
---
This project is intended for academic purposes only. Respect the license terms of used APIs and models.
