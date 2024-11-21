"""
This file contains the FastAPI code for the Image Captioning API. The API receives an image file, 
generates a caption for the image using the Blip Image Captioning model, 
and translates the caption to Arabic using the MarianMT model. 
The original and translated caption are then returned as a response.
"""

from fastapi import FastAPI, UploadFile, File
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from utils import translate
import io

app = FastAPI()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-large"
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Image Captioning API!"}


# Define the endpoint for generating captions
@app.post("/generate-caption")
async def generate_caption(file_upload: UploadFile = File(...)):
    try:
        print(f"Received file: {file_upload.filename}")
        image_data = await file_upload.read()
        image = Image.open(io.BytesIO(image_data))
        inputs = processor(images=image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        arabic_caption = translate.translate_text(caption)
        print({"caption": caption, "arabic_caption": arabic_caption})
        return {"english_caption": caption, "arabic_caption": arabic_caption}
    except Exception as e:
        return {"error": str(e)}
