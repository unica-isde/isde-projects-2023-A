import unittest
import base64
from bs4 import BeautifulSoup
import requests

class TestUpload(unittest.TestCase):
    def setUp(self):
        self.host = "localhost"
        self.port = "8000"
        self.api_name = "upload-and-classify"
        self.path_image_to_test = "app/static/test_images/"
        self.image_filename = "neural_net.png"

    def tearDown(self):
        del self.host
        del self.port
        del self.api_name
        del self.path_image_to_test

    """
    This class tests the file download functionalities of the application.
    """
    def test_image_loading(self):
        """
        Test if the classified image is was uploaded correctly
        """
        img_complete_path = self.path_image_to_test + self.image_filename

        with open(img_complete_path, "rb") as file:
            # Conversion to base64 format of test image
            img_raw_bytes = file.read()

            # Prepare user-like form, with model_id and choosen file
            form_data = {
                "model_id": "inception_v3"
            }

            files = {
            "image": (self.path_image_to_test, img_raw_bytes, "image/jpeg"),
            }
            #print(img_raw_bytes)
            # Perform a http post request to localhost
            response = requests.post(
                f"http://{self.host}:{self.port}/{self.api_name}",
                data = form_data,
                files = files
                )
            # Check if the request was successful
            self.assertEqual(response.status_code, 200, "The status code is not 200")

            # Parse the HTML response
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the img tag
            img_tag = soup.find("img", class_="large-front-thumbnail")

            # Extract the src attribute from the img tag
            src_attribute = img_tag.get("src")

            # Extract the base64 part from the src attribute
            _, base64_part = src_attribute.split(",", 1)

            # Convert original image bytes to base 64
            base64_image = base64.b64encode(img_raw_bytes).decode('utf-8')

            # Compare the base64 from the response with the original base64
            self.assertEqual(base64_part, base64_image, f"Error uploading the image in /{self.api_name} api")

if __name__ == '__main__':
    unittest.main()

