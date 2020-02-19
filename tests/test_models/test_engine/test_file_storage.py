#!/usr/bin/python3
"""This module contains the testing class for the file storage"""
import unittest
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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

    def testStoreState(self):
        """Tests that a State can me stored and reloaded"""
        s1 = State()

        fs.save()
        FileStorage._FileStorage__objects = {}

        fs.reload()

        self.assertIn("State.{}".format(s1.id), models.storage.all().keys())

    def testStoreCity(self):
        """Tests that a City can me stored and reloaded"""
        s1 = City()

        fs.save()
        FileStorage._FileStorage__objects = {}

        fs.reload()

        self.assertIn("City.{}".format(s1.id), models.storage.all().keys())

    def testStorePlace(self):
        """Tests that a Place can me stored and reloaded"""
        s1 = Place()

        fs.save()
        FileStorage._FileStorage__objects = {}

        fs.reload()

        self.assertIn("Place.{}".format(s1.id), models.storage.all().keys())

    def testStoreReview(self):
        """Tests that a Review can me stored and reloaded"""
        s1 = Review()

        fs.save()
        FileStorage._FileStorage__objects = {}

        fs.reload()

        self.assertIn("Review.{}".format(s1.id), models.storage.all().keys())
