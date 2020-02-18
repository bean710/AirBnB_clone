"""Module for testing the Base class"""
import unittest
import time
from models.city import City


class TestCityClass(unittest.TestCase):
    """Tests the city class"""

    def testName(self):
        """Tests the name attribute"""
        self.assertIs(type(City.name), str)

    def testId(self):
        """Tests the id attribute"""
        self.assertIs(type(City.state_id), str)
