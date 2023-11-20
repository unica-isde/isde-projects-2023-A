import unittest

from app.forms.classification_form_histogram import ClassificationFormHistogram


class ClassificationHistogramTest(unittest.TestCase):

    def setUp(self):
        self.image_id = "n01440764_tench.JPEG"
        self.histogram_dummy = ClassificationFormHistogram(self.image_id)
        pass

    def test_create_histogram_form(self):
        image_id = "n01440764_tench.JPEG"
        histogram = ClassificationFormHistogram(image_id)
        self.assertEqual(self.histogram_dummy, histogram)

    def test_is_valid(self):
        image_id = "n01440764_tench.JPEG"
        histogram = ClassificationFormHistogram(image_id)
        self.assertEqual(histogram.is_valid(), True)

    def test_is_not_valid(self):
        image_id = ""
        histogram = ClassificationFormHistogram(image_id)
        self.assertEqual(histogram.is_valid(), False)

