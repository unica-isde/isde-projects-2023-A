import unittest
from bs4 import BeautifulSoup


class TestOutputHistogram(unittest.TestCase):
    """
    This class asserts the classification output histogram page.
    """
    def test_canvas_output(self):
        """
        Test if the canvas is present in the classification output histogram page.
        """
        with open("app/templates/classification_output_histogram.html") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            canvas_image = soup.find("canvas", {"id": "histogramCanvas"})
            self.assertIsNotNone(canvas_image, "There is no canvas in the html page")

    def test_back_button(self):
        """
        Test if the back button is present in the classification output histogram page.
        """
        with open("app/templates/classification_output_histogram.html") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            back_button = soup.find("a", {"id": "backButton", "role": "button"})
            self.assertIsNotNone(back_button, "There is no back button in the html page")

    def test_img_showed(self):
        """
        Test if the image is present in the classification output histogram page.
        """
        with open("app/templates/classification_output_histogram.html") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            img = soup.find("img", {"id": "selectedImage"})
            self.assertIsNotNone(img, "There is no image in the html page")


if __name__ == '__main__':
    unittest.main()
