from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util

# Load KeyBERT
kw_model = KeyBERT()

# Load Sentence Transformer for similarity
sim_model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_skills_from_jd_keywords(jd_text):
    keywords = kw_model.extract_keywords(jd_text, top_n=10, stop_words='english')
    return [kw[0] for kw in keywords]

def compare_resume_with_jd(resume_text, jd_text):
    jd_embedding = sim_model.encode(jd_text, convert_to_tensor=True)
    resume_embedding = sim_model.encode(resume_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding)
    score_percentage = round(float(similarity.item()) * 100, 2)
    return score_percentage
