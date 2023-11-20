import unittest
import os
from PIL import Image
from app.ml.classification_utils import fetch_image

from app.config import Configuration

conf = Configuration()

class FetchImageTest(unittest.TestCase):

    def test_fetch_image(self):
        image_id = "n01440764_tench.JPEG"
        expected_image_path = os.path.join(conf.image_folder_path, image_id)
        expected_image = Image.open(expected_image_path)

        actual_image = fetch_image(image_id)

        self.assertEqual(actual_image, expected_image)


if __name__ == '__main__':
    unittest.main()