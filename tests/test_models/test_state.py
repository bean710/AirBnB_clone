"""Module for testing the Base class"""
import unittest
import time
from models.state import State


class TestStateClass(unittest.TestCase):
    """Tests the state class"""

    def testName(self):
        """Tests the name attribute"""
        self.assertIs(type(State.name), str)
