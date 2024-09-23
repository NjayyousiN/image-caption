from fastapi import FastAPI, UploadFile, File   
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image 
import io

app = FastAPI()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    inputs = processor(images=image, return_tensors="pt")
    
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)

    return {"caption": caption}
