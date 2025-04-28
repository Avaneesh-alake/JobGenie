import pandas as pd
from datasets import Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration
from sklearn.metrics import jaccard_score
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud


# Load your fine-tuned model
model_path = "models/jd_skill_extractor/final_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

# Helper to flatten lists
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# Load the clean dataset
test_df = pd.read_csv("datasets/jd_to_skills_clean.csv", quotechar='"')  
test_df["input_text"] = "extract key skills only: " + test_df["input_text"]
dataset = Dataset.from_pandas(test_df)
dataset = dataset.train_test_split(test_size=0.2)

# Prepare inputs and labels
test_data = dataset["test"]

y_true = []
y_pred = []

print("\n--- Evaluation Metrics ---")
print(f"Total test samples: {len(test_data)}")

for sample in test_data:
    input_text = sample["input_text"]
    target_text = sample["target_text"]

    # Tokenize input and generate prediction
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
    outputs = model.generate(inputs["input_ids"], max_length=64, num_beams=4, early_stopping=True)

    # Decode output
    pred_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Parse skills as list
    true_skills = [skill.strip().lower() for skill in target_text.split(",") if skill.strip()]
    pred_skills = [skill.strip().lower() for skill in pred_text.split(",") if skill.strip()]

    y_true.append(true_skills)
    y_pred.append(pred_skills)

# Get all unique skills
all_skills = list(set(flatten(y_true) + flatten(y_pred)))

# Binarize
def binarize(skills_list):
    return [1 if skill in skills_list else 0 for skill in all_skills]

y_true_bin = [binarize(skills) for skills in y_true]
y_pred_bin = [binarize(skills) for skills in y_pred]

# Calculate Jaccard Scores
micro_jaccard = jaccard_score(y_true_bin, y_pred_bin, average="micro")
macro_jaccard = jaccard_score(y_true_bin, y_pred_bin, average="macro")

print(f"\nMicro Jaccard Score: {micro_jaccard:.2f}")
print(f"Macro Jaccard Score: {macro_jaccard:.2f}")

# =============================
# Plot Training Loss (Simulated)
# =============================

# Create dummy loss curve (just for plot)
epochs = list(range(1, 11))
loss = [5.2, 4.8, 4.1, 3.9, 3.6, 3.2, 2.9, 2.7, 2.5, 2.3]

# Create plots folder if not exist
os.makedirs("plots", exist_ok=True)

# Plot
plt.figure()
plt.plot(epochs, loss, marker='o')
plt.title("Training Loss vs Epochs (Simulated)")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)
plt.savefig("plots/loss_curve.png")
plt.show()

# =============================
# Additional: Per-Sample Jaccard Scores Plot
# =============================
sample_scores = []
for true, pred in zip(y_true_bin, y_pred_bin):
    score = jaccard_score([true], [pred], average="micro")
    sample_scores.append(score)

# Plot
plt.figure(figsize=(10,6))
plt.bar(range(len(sample_scores)), sample_scores, color='skyblue')
plt.xlabel("Test Sample Index")
plt.ylabel("Jaccard Score")
plt.title("Per-Sample Jaccard Scores (Fine-Tuned Model)")
plt.ylim(0, 1)
plt.grid(axis='y')

# Save plot
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/sample_jaccard_scores.png")
plt.show()

# =============================
# Additional: True vs Predicted Skills Count
# =============================
true_counts = [len(skills) for skills in y_true]
pred_counts = [len(skills) for skills in y_pred]

plt.figure(figsize=(10,6))
plt.plot(range(len(true_counts)), true_counts, label="True Skills Count", marker='o')
plt.plot(range(len(pred_counts)), pred_counts, label="Predicted Skills Count", marker='x')
plt.title("True vs Predicted Skills per Sample")
plt.xlabel("Sample Index")
plt.ylabel("Number of Skills")
plt.legend()
plt.grid(True)
plt.savefig("plots/true_vs_predicted_counts.png")
plt.show()

# =============================
# Additional: WordCloud of Skills
# =============================
# Create word cloud from true skills
all_true_skills = flatten(y_true)

text = " ".join(all_true_skills)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title("WordCloud of True Skills")
plt.savefig("plots/skills_wordcloud.png")
plt.show()