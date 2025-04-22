
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util

# Initialize models
kw_model = KeyBERT(model='all-MiniLM-L6-v2')
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def extract_skills_from_jd(jd_text: str, num_keywords: int = 10):
    keywords = kw_model.extract_keywords(jd_text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_keywords)
    return [kw[0] for kw in keywords]

def compare_resume_with_jd(resume_text: str, jd_text: str):
    resume_embedding = embedder.encode(resume_text, convert_to_tensor=True)
    jd_embedding = embedder.encode(jd_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding).item()
    score = round(similarity * 100, 2)
    return score
