from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from .model_handler import generate_image


app = FastAPI()

@app.post("/generate")
def generate(prompt: str = Form(...), negative_prompt: str = Form(""), width: int = Form(512), height: int = Form(512)):
    image_path = generate_image(prompt, negative_prompt, width, height)
    return FileResponse(image_path, media_type="image/png")

MODELS_DIR = "backend/models"

@app.get("/models")
def list_models():
    models = []
    if os.path.exists(MODELS_DIR):
        for item in os.listdir(MODELS_DIR):
            full_path = os.path.join(MODELS_DIR, item)
            if os.path.isdir(full_path):
                models.append(item)
    return JSONResponse(content={"models": models})