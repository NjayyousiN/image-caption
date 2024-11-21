'''
This file contains the code to translate text from English to Arabic using the MarianMTModel from the transformers library.
The translate_text function takes an English text as input, tokenizes it, generates the translation, and decodes the translated text.
'''

from transformers import MarianTokenizer, MarianMTModel, Seq2SeqTrainingArguments, Seq2SeqTrainer

model_name = "Helsinki-NLP/opus-mt-en-ar"
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Load Model and Define Training Arguments
model = MarianMTModel.from_pretrained(model_name)

# Function to translate text
def translate_text(text):
    # Prepare the input text with the appropriate language token (if required)
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
    
    # Generate translation
    translated = model.generate(**inputs)
    
    # Decode the translated text
    output = tokenizer.decode(translated[0], skip_special_tokens=True)
    return output

