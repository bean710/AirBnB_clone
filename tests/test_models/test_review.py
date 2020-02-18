"""Module for testing the Base class"""
import unittest
import time
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Tests the review class"""

    def testPlaceId(self):
        """Tests the place_id attribute"""
        self.assertIs(type(Review.place_id), str)

    def testUserId(self):
        """Tests the user_id attribute"""
        self.assertIs(type(Review.user_id), str)

    def testText(self):
        """Tests the text attribute"""
        self.assertIs(type(Review.text), str)
