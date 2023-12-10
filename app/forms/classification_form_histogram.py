from typing import List
from fastapi import Request


class ClassificationFormHistogram:
    def __init__(self, image_id: str) -> None:
        self.image_id = image_id
        self.errors: List = []

    def set_image_id(self, image_id: str) -> None:
        self.image_id = image_id

    async def load_data(self, request: Request) -> None:
        form = await request.form()
        self.image_id = form.get("image_id")

    def is_valid(self):
        if not self.image_id or not isinstance(self.image_id, str):
            self.errors.append("A valid image id is required")
        if not self.errors:
            return True
        return False
