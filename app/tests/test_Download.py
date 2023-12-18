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
        with open("app/templates/classification_output.html") as f:
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


if __name__ == '__main__':
    unittest.main()
