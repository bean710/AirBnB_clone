#!/usr/bin/python3
"""Module for testing the Base class"""
import unittest
import time
from models.base_model import BaseModel
from datetime import datetime
import json

class TestBaseClass(unittest.TestCase):
    """Contains functions for testing aspects of the base class"""

    def testId(self):
        """Tests that a unique ID is assigned to each BaseModel"""
        bma = BaseModel()
        bmb = BaseModel()

        self.assertNotEqual(bma.id, bmb.id)

    def testStringify(self):
        """Tests that the str method for a BaseModel"""
        bma = BaseModel()
        self.assertRegex(str(bma), "\[.+\] (.+) {.+}")

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

    def testSave(self):
        """Tests that save updates the time"""
        bma = BaseModel()
        a_time = bma.updated_at
        time.sleep(0.001)
        bma.save()

        self.assertNotEqual(a_time, bma.updated_at)

        with open("data.json", "r") as f:
            self.assertIn(bma.to_dict(), json.loads(f.read()).values())

    def testInit(self):
        """Tests init given a dictionary"""
        bma = BaseModel()
        bma.my_num = 47;

        bmb = BaseModel(**bma.to_dict())

        self.assertEqual(bma.id, bmb.id)
        self.assertEqual(bma.created_at, bmb.created_at)
        self.assertEqual(bma.updated_at, bmb.updated_at)
        self.assertEqual(bmb.my_num, 47)

    def testMethod(self):
        """Check for methods in BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def testattr(self):
        """Test to see if instance was properly created"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "__init__"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertTrue(hasattr(bm, "id"))
