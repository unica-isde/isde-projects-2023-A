import unittest
from app.forms.classification_form_histogram import ClassificationFormHistogram
from app.tests import constants


class ClassificationHistogramTest(unittest.TestCase):

    def setUp(self):
        self.image_id = constants.TEST_IMAGE_ID
        self.histogram_dummy = ClassificationFormHistogram(self.image_id)
        print(self.histogram_dummy.image_id)

    def test_create_histogram_form(self):
        histogram = ClassificationFormHistogram(constants.TEST_IMAGE_ID)
        self.assertEqual(self.histogram_dummy.image_id, histogram.image_id)
        pass

    def test_is_valid(self):
        histogram = ClassificationFormHistogram(constants.TEST_IMAGE_ID)
        self.assertTrue(histogram.is_valid())

    def test_is_not_valid(self):
        histogram = ClassificationFormHistogram("")
        self.assertFalse(histogram.is_valid())


if __name__ == '__main__':
    unittest.main()
