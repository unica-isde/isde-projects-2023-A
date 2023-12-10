import json
from typing import Dict, List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import redis
from rq import Connection, Queue
from rq.job import Job
from app.config import Configuration
from app.forms.classification_form import ClassificationForm
from app.forms.classification_form_histogram import ClassificationFormHistogram
from app.ml.classification_utils import classify_image
from app.ml.classification_utils import fetch_image
from app.utils import list_images
from io import BytesIO
import base64

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
    return templates.TemplateResponse(
        "classification_output.html",
        {
            "request": request,
            "image_id": image_id,
            "classification_scores": json.dumps(classification_scores),
        },
    )


@app.get("/classifications_histogram")
def create_classify(request: Request):
    """
    This function is used to create the classification page for the histogram method.
        Parameters
        ----------
        request: Request
            The request object.

        Returns
        -------
        templates.TemplateResponse
            The template response with the request and the list of images.
    """
    return templates.TemplateResponse(
        "classification_select_histogram.html",
        {"request": request, "images": list_images()},
    )


@app.post("/classifications_histogram")
    
async def request_classification(request: Request):
    """
    This function is used to classify the image using the histogram method.
        Parameters
        ----------
        request: Request
            The request object.

        Returns
        -------
        templates.TemplateResponse
            The template response with the request, image_id and the image as base64 string.
    """
    form = ClassificationFormHistogram("")
    await form.load_data(request)
    image_id = form.image_id
    img = fetch_image(image_id)
    # convert image to base64 string to display in html
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return templates.TemplateResponse(
        "classification_output_histogram.html",
        {
            "request": request,
            "image_id": image_id,
            "image": img_str,
        },
    )
