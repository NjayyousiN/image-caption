from transformers import MarianMTModel, MarianTokenizer
import torch

# Load the model and tokenizer (already done earlier)
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ar")

# Determine the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def translate_text(text):
    # Encode the text
    encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    
    # Move inputs to the appropriate device
    encoded_input = {key: value.to(device) for key, value in encoded_input.items()}
    
    # Perform translation
    translated = model.generate(**encoded_input, max_new_tokens=1000)
        
    # Decode the translated text
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    return translated_text[0]
# print("Translation:", translate_text("There is a red rose in a garden with water droplets on it."))