"""Module for testing the Base class"""
import unittest
import time
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Tests the amenity class"""

    def testName(self):
        """Tests the name attribute"""
        self.assertIs(type(Amenity.name), str)
