from typing import List
from fastapi import Request
#app.forms.classification_form import ClassificationForm

from app.forms.classification_form import ClassificationForm

class ClassificationTransformForm(ClassificationForm):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.color: float
        self.brightness: float
        self.contrast: float
        self.sharpness: float

    async def load_data(self):
        form = await self.request.form()
        self.image_id = form.get("image_id")
        self.model_id = form.get("model_id")
        self.color = float(form.get("color"))
        self.brightness = float(form.get("brightness"))
        self.contrast = float(form.get("contrast"))
        self.sharpness = float(form.get("sharpness"))

    def is_valid(self):
        super().is_valid()
