#!/usr/bin/python3
"""This module contains the testing class for the file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json

fs = FileStorage()

class TestFileStorage(unittest.TestCase):
    """Class contains testing methods"""

    original_path = ""

    def setUp(self):
        """Resets the file storage class for each test"""
        FileStorage._FileStorage__objects = {}
        TestFileStorage.original_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Removes test json file"""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = TestFileStorage.original_path

    def testAll(self):
        """Tests that the all method works to get all objects"""
        dicts = {"BaseModel.0001":{"foo":1, "Bar":2},
                 "BaseModel.0002":{"Ben":47, "Keener":29}}

        FileStorage._FileStorage__objects = dicts

        self.assertEqual(dicts, fs.all())

    def testNew(self):
        """Tests that an object can be added to the storage"""
        bma = BaseModel()
        fs.new(bma)

        self.assertIs(type(fs.all()), dict)
        self.assertEqual(fs.all()["BaseModel." + bma.id], bma)

    def testSave(self):
        """Tests that the storage can be saved to a file"""
        bma = BaseModel()
        bmb = BaseModel()

        fs.new(bma)
        fs.new(bmb)

        fs.save()

        with open("test.json", "r") as f:
            self.assertEqual(json.loads(f.read()), {k:v.to_dict() for k, v in
                                                    fs.all().items()})

    def testReload(self):
        """Tests that the storage can be loaded from a file"""
        bma = BaseModel()
        bmb = BaseModel()

        bmb.name = "FooBar"

        og_all = fs.all().copy()
        og_all_dict = {k:v.to_dict() for k, v in og_all.items()}
        fs.save()

        FileStorage._FileStorage__objects = {}

        fs.reload()

        self.maxDiff = None
        self.assertEqual(og_all_dict, {k:v.to_dict() for k, v in fs.all().items()})
