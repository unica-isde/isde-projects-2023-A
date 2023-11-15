import unittest
from bs4 import BeautifulSoup
import requests
import base64


class TestDownload(unittest.TestCase):
    """
    This class tests the file download functionalities of the application.
    """

    def test_buttonsInInterface(self):
        """
        Test if the buttons are in the html page and have the right text.
        """
        with open("../templates/classification_output.html") as f:
            html = f.read()
            soup = BeautifulSoup(html, "html.parser")

            # Find the button with id "downloadResultsButton"
            button = soup.find("a", {"id": "downloadResultsButton", "role": "button"})

            # Check if the button with "a" tag and "role:button" is in the html page
            self.assertIsNotNone(button, "There is no button with id 'downloadResultsButton' in the html page")

            # Check if the button has the right text
            self.assertEqual(button.text, "Download results", "The button has not the right text")

            # Find the button with id "downloadPlotButton"
            button = soup.find("a", {"id": "downloadPlotButton", "role": "button"})

            # Check if the button is in the html page
            self.assertIsNotNone(button, "There is no button with id 'downloadPlotButton' in the html page")

            # Check if the button has the right text
            self.assertEqual(button.text, "Download plot", "The button has not the right text")

    def test_jsonIsCorrect(self):
        """
        Test if the json file is not empty.
        """
        # Make a request to the endpoint that returns the json file
        response = requests.get("http://localhost:8000/downloadResults")

        # Check if the response is not empty and it is a json file
        self.assertIsNotNone(response, "The json file is empty")
        self.assertEqual(response.headers["Content-Type"], "application/json", "The file is not a json file")

    def test_plotIsCorrect(self):
        """
        Test if the plot is not empty.
        """
        # Open an image and encode it in base 64
        with open("../static/plot.png", "rb") as f:
            base64image = base64.b64encode(f.read())

            # Create a dict with the base 64 encoded image with JSON format
            payload = {"ctx": base64image.decode("utf-8")}

            # Make a request to the endpoint that returns the plot, Put in the body the base 64 encoded image as a dict
            response = requests.post("http://localhost:8000/downloadPlot", json=payload)

            # Check if the response is not empty and it is a png file
            self.assertIsNotNone(response, "The plot is empty")
            self.assertEqual(response.headers["Content-Type"], "image/png", "The file is not a png file")
            self.assertEqual(response.headers["Content-Disposition"], "attachment; filename=\"plot.png\"",
                             "The file is not a png file")
            self.assertEqual(response.status_code, 200, "The status code is not 200")
