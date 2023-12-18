from typing import List
from fastapi import Request
from starlette import datastructures
from app.config import Configuration

class ClassificationUploadForm:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.errors: List = []
        self.model_id: str
        self.image: datastructures.UploadFile
        self.image_bytes: bytes

    async def load_data(self):
        form = await self.request.form()
        self.model_id = form.get("model_id")
        self.image = form.get("image")

        if self.image is not None:
            self.image_bytes = self.image.file.read()

    def is_valid(self):
        if not self.model_id or not isinstance(self.model_id,str):
            self.errors.append("A valid model id is required")
        
        if not self.image or not isinstance(self.image, datastructures.UploadFile):
            self.errors.append("Upload a valid image. Is required")

        elif not self.image.content_type in Configuration.img_allowed_formats:
            self.errors.append(f"A valid format is required, like = {Configuration.img_allowed_formats}")

        if len(self.image_bytes) == 0:
            self.errors.append("Upload a non-empty image")
        
        if not self.errors:
            return True
        return False
