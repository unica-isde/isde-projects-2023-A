import unittest
import base64
from bs4 import BeautifulSoup
import requests

class TestUpload(unittest.TestCase):
    def setUp(self):
        self.host = "localhost"
        self.port = "8000"
        self.api_name = "upload-and-classify"
        self.path_image_to_test = "app/static/test_images/neural_net.png"

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

        with open(self.path_image_to_test, "rb") as file:
            # Conversion to base64 format of test image
            base64image = base64.b64encode(file.read())

            # Prepare user-like form, with model_id and choosen file 
            form_data = {
                "model_id": "inception_v3"
            }

            files = {"image": (file.name, file, "image/jpeg")}
            
            # Perform a http post request to localhost
            response = requests.post(
                f"http://{self.host}:{self.port}/{self.api_name}", 
                data = form_data, 
                files = files)

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

            # Compare the base64 from the response with the original base64
            self.assertEqual(base64_part, base64image, f"Error uploading the image in /{self.api_name} api")
    
if __name__ == '__main__':
    unittest.main()
        
