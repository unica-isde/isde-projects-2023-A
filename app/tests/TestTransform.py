import unittest
from bs4 import BeautifulSoup

class MyTestCase(unittest.TestCase):
    """
    This class tests the interface of the classification transformation page.
    """
    def test_button_interface(self):
        """
        Test if the inputs are present in the classification transformation page.
        """
        with open("../templates/classification_transform_select.html") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            inputcolor= soup.find("input", {"name": "color"})
            self.assertIsNotNone(inputcolor)
            inputbrightness= soup.find("input", {"name": "brightness"})
            self.assertIsNotNone(inputbrightness)
            inputcontrast= soup.find("input", {"name": "contrast"})
            self.assertIsNotNone(inputcontrast)
            inputsharpness= soup.find("input", {"name": "sharpness"})
            self.assertIsNotNone(inputsharpness)

if __name__ == '__main__':
    unittest.main()
