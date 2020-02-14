#!/usr/bin/python3
"""This module contains the file storage class"""
import json
import models
import models.base_model
import models.user

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
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes storage to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps({k:v.to_dict() for k,v in
                                FileStorage.__objects.items()}))

    def reload(self):
        """Reloads the file storage"""
        tmp = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp = json.loads(f.read())
        except:
            pass
        else:
            for k, v in tmp.items():
                ## ---> FileStorage.__objects[k] = getattr(models.base_model, v["__class__"])(**v)
                if (v["__class__"] == "BaseModel"):
                    FileStorage.__objects[k] = models.base_model.BaseModel(**v)
                elif (v["__class__"] == "User"):
                    FileStorage.__objects[k] = models.user.User(**v)
