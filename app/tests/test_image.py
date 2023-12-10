import unittest
import os
import sys
from PIL import Image
from main import app
from app.ml.classification_utils import fetch_image_file

from app.config import Configuration

conf = Configuration()

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, project_dir)


class FetchImageTest(unittest.TestCase):

    def test_fetch_image(self):
        image_id = "n01440764_tench.JPEG"
        expected_image_path = os.path.join(conf.image_folder_path, image_id)
        expected_image = Image.open(expected_image_path)

        actual_image = fetch_image_file(image_id)

        self.assertEqual(actual_image, expected_image)


if __name__ == '__main__':
    unittest.main()