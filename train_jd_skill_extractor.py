
from datasets import load_dataset, Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
import pandas as pd
import torch

#Load CSV into Hugging Face Dataset
df = pd.read_csv("datasets/jd_to_skills.csv")
df["input_text"] = "extract skills: " + df["input_text"]
dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.2)

# Load tokenizer and model
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Tokenize dataset
def tokenize(example):
    input_enc = tokenizer(example["input_text"], truncation=True, padding="max_length", max_length=128)
    target_enc = tokenizer(example["target_text"], truncation=True, padding="max_length", max_length=64)
    input_enc["labels"] = target_enc["input_ids"]
    return input_enc

tokenized = dataset.map(tokenize)

# Define training arguments
training_args = TrainingArguments(
    output_dir="models/jd_skill_extractor",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=10,
    logging_dir="logs/jd_skill_logs"
)



# Create Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer
)

#Train the model
trainer.train()

# Save model locally
trainer.save_model("models/jd_skill_extractor")
tokenizer.save_pretrained("models/jd_skill_extractor")
