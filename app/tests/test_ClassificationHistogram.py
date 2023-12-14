import unittest
from app.forms.classification_form_histogram import ClassificationFormHistogram
from app.tests import constants


class ClassificationHistogramTest(unittest.TestCase):
    """
    This class tests the classification histogram form.
    """
    def setUp(self):
        """
        This method is called before each test is executed.
        """
        self.image_id = constants.TEST_IMAGE_ID
        self.histogram_dummy = ClassificationFormHistogram(self.image_id)

    def tearDown(self):
        """
        This method is called after each test is executed.
        """
        del self.image_id
        del self.histogram_dummy

    def test_create_histogram_form(self):
        """
        This method tests the creation of the histogram form.
        """
        histogram = ClassificationFormHistogram(constants.TEST_IMAGE_ID)
        self.assertEqual(self.histogram_dummy.image_id, histogram.image_id)
        pass

    def test_is_valid(self):
        """
        This method tests the is_valid method of the histogram form.
        """
        histogram = ClassificationFormHistogram(constants.TEST_IMAGE_ID)
        self.assertTrue(histogram.is_valid())

    def test_is_not_valid(self):
        """
        This method tests the is_valid method of the histogram form in case the imageId passed is empty.
        """
        histogram = ClassificationFormHistogram("")
        self.assertFalse(histogram.is_valid())


if __name__ == '__main__':
    unittest.main()
