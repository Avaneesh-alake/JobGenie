from keybert import KeyBERT
from transformers import T5ForConditionalGeneration, T5Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Existing model
kw_model = KeyBERT()

# Fine-tuned Flan-T5 model
model_path = "models/jd_skill_extractor/final_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

# Method 1 - Keyword extractor (existing)
def extract_skills_from_jd_keywords(jd_text):
    keywords = kw_model.extract_keywords(jd_text, top_n=10, stop_words='english')
    return [kw[0] for kw in keywords]

# Method 2 - Fine-tuned model
def extract_skills_from_jd_finetuned(jd_text):
    prompt = "extract key skills only: " + jd_text
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
    output_ids = model.generate(inputs["input_ids"], max_length=64, num_beams=4, early_stopping=True)
    
    raw_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    skills = list(set(skill.strip() for skill in raw_output.split(",") if skill.strip()))
    
    return skills

def compare_resume_with_jd(resume_text, jd_text):
    texts = [resume_text, jd_text]
    tfidf = TfidfVectorizer().fit_transform(texts)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)