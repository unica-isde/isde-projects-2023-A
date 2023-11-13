import json
from typing import Dict, List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import Configuration
from app.forms.classification_form import ClassificationForm
from app.ml.classification_utils import classify_image
from app.utils import list_images
from fastapi import FastAPI
import base64
from PIL import Image
from io import BytesIO


app = FastAPI()
config = Configuration()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/info")
def info() -> Dict[str, List[str]]:
    """Returns a dictionary with the list of models and
    the list of available image files."""
    list_of_images = list_images()
    list_of_models = Configuration.models
    data = {"models": list_of_models, "images": list_of_images}
    return data


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """The home page of the service."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/classifications")
def create_classify(request: Request):
    return templates.TemplateResponse(
        "classification_select.html",
        {"request": request, "images": list_images(), "models": Configuration.models},
    )


@app.post("/classifications")
async def request_classification(request: Request):
    form = ClassificationForm(request)
    await form.load_data()
    image_id = form.image_id
    model_id = form.model_id
    classification_scores = classify_image(model_id=model_id, img_id=image_id)
    with open("app/static/results.json", "w") as f: #TODO asks if this has to be unique or shared between users
        json.dump(classification_scores, f)
    return templates.TemplateResponse(
        "classification_output.html",
        {
            "request": request,
            "image_id": image_id,
            "classification_scores": json.dumps(classification_scores),
        },
    )

@app.get("/downloadResults")
def download_results():
    return FileResponse("app/static/results.json", media_type="application/json", filename="results.json")

@app.post("/downloadPlot")
def download_plot(ctx: dict):
    # Retrieve the image url from the context
    image_url = ctx.get("ctx")

    # Rimuovi l'intestazione del formato dell'immagine (es. "data:image/png;base64,")
    base64_data = image_url.split(',')[1]

    # Decodifica il dato base64
    image_data = base64.b64decode(base64_data)

    # Creare un oggetto di immagine utilizzando il modulo Pillow (PIL)
    image = Image.open(BytesIO(image_data))

    # Salva l'immagine come file PNG
    image.save("app/static/plot.png", "PNG")

    return FileResponse("app/static/plot.png", media_type="image/png", filename="plot.png")