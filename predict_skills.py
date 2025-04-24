
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the fine-tuned model and tokenizer
# model_path = "models/jd_skill_extractor/checkpoint-40"
model_path = "models/jd_skill_extractor/final_model"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

def extract_skills_from_jd(jd_text):
    prompt = "extract key skills only: " + jd_text
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
    output_ids = model.generate(inputs["input_ids"], max_length=64, num_beams=4, early_stopping=True)
    # Decode model output
    raw_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    # Postprocess: return unique, trimmed list of skills
    skills = list(set(skill.strip() for skill in raw_output.split(",") if skill.strip()))
    return skills


# Test with a new JD
# jd = "We are hiring a DevOps engineer with experience in Jenkins, Docker, and AWS."
# jd = "Looking for a cloud architect skilled in AWS, Terraform, and Kubernetes."
jd = "We are hiring a DevOps engineer familiar with Jenkins, Docker, and AWS EC2."
predicted_skills = extract_skills_from_jd(jd)

print("\n Job Description:\n", jd)
print("\n Extracted Skills List:\n", predicted_skills)
