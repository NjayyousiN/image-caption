import random
from datasets import load_dataset

# Load the full dataset
file_path = 'backend/data/ara_eng.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Shuffle the lines to randomize the data
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

dataset = load_dataset('text', data_files={
    'train': 'backend/data/train_ara_eng.txt',
    'validation': 'backend/data/val_ara_eng.txt'
})

# Map the data into a dictionary format
def split_line(example):
    en, ar = example['text'].split('\t')
    return {'translation': {'en': en, 'ar': ar}}

model_dataset = dataset.map(split_line)

