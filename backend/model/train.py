'''
This script trains a MarianMT model on the Arabic-English dataset. The dataset is loaded from a text file, 
split into training and validation sets, and then loaded into the Hugging Face Dataset format. 
The dataset is tokenized using the MarianTokenizer, and the model is fine-tuned using the Seq2SeqTrainer.
The trained model is then saved to disk for later use. The script also evaluates the model on the validation set (BLEU).
'''
from transformers import MarianTokenizer, MarianMTModel, Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import load_dataset
import random

# Load and split dataset
file_path = 'backend/data/ara_eng.txt'  # Adjust for Colab's file system
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Shuffle the lines
random.shuffle(lines)

# Split the dataset
train_ratio = 0.8
split_index = int(len(lines) * train_ratio)

train_lines = lines[:split_index]
val_lines = lines[split_index:]

# Save the training and validation files
with open('backend/data/train_ara_eng.txt', 'w', encoding='utf-8') as train_file:
    train_file.writelines(train_lines)

with open('backend/data/val_ara_eng.txt', 'w', encoding='utf-8') as val_file:
    val_file.writelines(val_lines)

print(f"Training set: {len(train_lines)} lines")
print(f"Validation set: {len(val_lines)} lines")

# Load dataset into Hugging Face Dataset format
dataset = load_dataset('text', data_files={
    'train': 'backend/data/train_ara_eng.txt',
    'validation': 'backend/data/val_ara_eng.txt'
})

# Map data into dictionary format
def split_line(example):
    en, ar = example['text'].split('\t')
    return {'translation': {'en': en.strip(), 'ar': ar.strip()}}

model_dataset = dataset.map(split_line)

# Tokenize dataset
from transformers import MarianTokenizer, MarianMTModel, Seq2SeqTrainer, Seq2SeqTrainingArguments

model_name = "Helsinki-NLP/opus-mt-en-ar"
tokenizer = MarianTokenizer.from_pretrained(model_name)

def tokenize_function(examples):
    inputs = [ex['en'] for ex in examples['translation']]
    targets = [ex['ar'] for ex in examples['translation']]
    return tokenizer(inputs, text_target=targets, padding='max_length', truncation=True, max_length=512)

tokenized_dataset = model_dataset.map(tokenize_function, batched=True)

# Load Model and Define Training Arguments
model = MarianMTModel.from_pretrained(model_name)

training_args = Seq2SeqTrainingArguments(
    output_dir="./fine_tuned_model",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2,
    predict_with_generate=True,
    logging_dir="./logs",
    logging_steps=200,
)

# Trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['validation'],
    tokenizer=tokenizer,
)

# Train and Save the Model
trainer.train()
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

# Evaluate Model
metrics = trainer.evaluate()
print(metrics)