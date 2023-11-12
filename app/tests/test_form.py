import unittest
import asyncio
from fastapi import Request

# ****** internals libs
from forms import ClassificationForm

class TestForm(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_form_api_classification(self):
        """
        The following test is used to verify that the classification
        form class correctly parses the fields of an HTTP POST request.
        this test replicates the form in the /classifications api
        """

        # examples of user choose from form.
        form_data = {
            "image_id": "n15075141_toilet_tissue.JPEG",
            "model_id": "inception_v3",
        }

        # prepare the request
        request = Request({"type": "http", "method": "POST", "path": "/classification"}, None, query_params = form_data)

        classification_form = ClassificationForm(request)

        # load form data with coroutine
        asyncio.run(classification_form.load_data())

        # check if our class has been parsed correctly
        self.assertEqual(classification_form.image_id, form_data["image_id"])
        self.assertEqual(classification_form.model_id, form_data["model_id"])

    def test_image_loading(self):
        pass
