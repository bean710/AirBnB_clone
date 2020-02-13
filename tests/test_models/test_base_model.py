#!/usr/bin/python3
"""Module for testing the Base class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseClass(unittest.TestCase):
    """Contains functions for testing aspects of the base class"""

    def testId(self):
        """Tests that a unique ID is assigned to each BaseModel"""
        bma = BaseModel()
        bmb = BaseModel()

        self.assertNotEqual(bma.id, bmb.id)

    def testCreationTime(self):
        """Tests that the creation time of a BaseModel is correct"""

    def testUpdateTime(self):
        """Tests that the update time of a BaseModel is correct"""

    def testStringify(self):
        """Tests that the str method for a BaseModel"""
        bma = BaseModel()
        self.assertRegex(str(bma), "\[.+\] (.+) <.+>")

    def testDict(self):
        """Tests the dictionary conversion"""
        bma = BaseModel()
        a_dict = bma.to_dict()

        self.assertIsNotNone(a_dict["id"])
        self.assertIsNotNone(a_dict["created_at"])
        self.assertIsNotNone(a_dict["updated_at"])
        self.assertIsNotNone(a_dict["__class__"])

        self.assertEqual(a_dict["__class__"], "BaseModel")

        self.assertRegex(a_dict["created_at"], "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+")
        self.assertRegex(a_dict["updated_at"], "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+")
