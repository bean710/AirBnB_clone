#!/usr/bin/python3
"""This module contains the file storage class"""
import json

class FileStorage():
    """The class that handles where and how the data is stored"""

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Gets all objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the storage dictionary"""
        key = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes storage to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Reloads the file storage"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
        except:
            pass
