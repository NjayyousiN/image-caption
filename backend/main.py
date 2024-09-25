from fastapi import FastAPI, UploadFile, File
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from utils import translate
import io
from fastapi.concurrency import run_in_threadpool

app = FastAPI()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # Processing the image and generating a caption
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)

    # Execute the synchronous translation in a thread pool to avoid blocking the async call
    arabic_caption = await run_in_threadpool(translate.translate_text, caption)

    return {"caption": caption, "arabic_caption": arabic_caption}
