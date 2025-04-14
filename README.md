# JobGenie: AI-Powered Career Assistant

**JobGenie** is a cloud-native, API-driven AI application that helps job seekers optimize their resumes, understand job descriptions, and practice mock interviews using Natural Language Processing (NLP) and Speech Recognition.

> Built as part of the **API-driven Cloud Native Solutions** course at BITS Pilani.

---

## Features

-  **Resume Rewriter**  
  Rewrites resume sections in a professional tone using LLMs.

-  **Job Description Analyzer** *(coming soon)*  
  Extracts key skills and matches them with resume content.

-  **Voice-based Interview Assistant** *(coming soon)*  
  Ask/Answer mock interview questions using speech-to-text.

-  **LLMOps Metrics Dashboard** *(coming soon)*  
  Tracks response time, token usage, accuracy, and cost.

---

## 🔧 Tech Stack

| Type             | Tools / Libraries                          |
|------------------|--------------------------------------------|
| Language         | Python                                     |
| NLP Models       | Hugging Face Transformers (`flan-t5-base`) |
| UI Interface     | Gradio                                     |
| Deployment Ready | Docker + AWS (EC2 / Lambda / S3)           |
| DevOps Ready     | `.env`, `requirements.txt`, version control |

---
## Local Setup
---
```bash
# Clone the repo
git clone https://github.com/your-username/JobGenie.git
cd JobGenie

# Create and activate virtual environment
python -m venv jobgenie-env
jobgenie-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

Note: Create a .env file in the root directory:
OPENAI_API_KEY=sk-xxxxx      # Optional (only if you switch to OpenAI)
```
---
License
---
This project is for academic purposes. All AI-generated content is subject to respective model licenses.
