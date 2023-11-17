from typing import List
from fastapi import Request


class ClassificationTransformForm:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.errors: List = []
        self.image_id: str
        self.model_id: str
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
        if not self.image_id or not isinstance(self.image_id, str):
            self.errors.append("A valid image id is required")
        if not self.model_id or not isinstance(self.model_id, str):
            self.errors.append("A valid model id is required")
        if not self.errors:
            return True
        return False
