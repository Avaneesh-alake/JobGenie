# JobGenie: AI-Powered Career Assistant

**JobGenie** is a cloud-native, API-driven AI application designed to help job seekers improve their resumes, analyze job descriptions, and prepare for interviews using Natural Language Processing (NLP) and Speech Recognition.

>  Built as part of the **API-driven Cloud Native Solutions** course at BITS Pilani.

---

## Features

### Resume Rewriter
Enhances resume sections using Hugging Face's `flan-t5-base`, allowing users to rewrite content in different tones for specific job roles.

### Job Description Analyzer
- Extracts top keywords and skills from a Job Description using `KeyBERT`
- Compares user’s resume content with the JD using `Sentence Transformers`
- Outputs a smart **Job Fit Score**

### Voice-based Interview Assistant *(Coming Soon)*
- Practice answering interview questions by voice
- Convert voice input to text using Whisper or sounddevice
- Get feedback on tone and coherence

### LLMOps Metrics Dashboard *(Coming Soon)*
- Track token usage, latency, relevance metrics, and cost insights

---

## 🛠️ Tech Stack

| Category         | Tools / Frameworks                          |
|------------------|---------------------------------------------|
| Language         | Python 3.10+                                |
| LLM Model        | Hugging Face Transformers (`flan-t5-base`)  |
| Skill Extraction | KeyBERT                                     |
| Similarity Model | Sentence Transformers (`MiniLM`)            |
| UI Interface     | Gradio                                      |
| Deployment Ready | Docker, AWS EC2 / Lambda                    |
| DevOps Ready     | `.env`, `requirements.txt`, Git             |

---

## Local Setup

```bash
# Clone the repo
git clone https://github.com/Avaneesh-alake/JobGenie.git
cd JobGenie

# Create and activate virtual environment
python -m venv jobgenie-env
jobgenie-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

```
---
License
---
This project is for academic purposes. All AI-generated content is subject to respective model licenses.
