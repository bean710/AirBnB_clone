#!/usr/bin/python3
"""This module contains the file storage class"""
import json
import models
import models.base_model
import models.user
import models.state
import models.city
import models.amenity
import models.place
import models.review


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
            f.write(json.dumps({k: v.to_dict() for k, v in
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
                # TODO: Is there a more ambiguous way to do this?
                cname = v["__class__"]
                if (cname == "BaseModel"):
                    FileStorage.__objects[k] = models.base_model.BaseModel(**v)
                elif (cname == "User"):
                    FileStorage.__objects[k] = models.user.User(**v)
                elif (cname == "State"):
                    FileStorage.__objects[k] = models.state.State(**v)
                elif (cname == "City"):
                    FileStorage.__objects[k] = models.city.City(**v)
                elif (cname == "Amenity"):
                    FileStorage.__objects[k] = models.amenity.Amenity(**v)
                elif (cname == "Place"):
                    FileStorage.__objects[k] = models.place.Place(**v)
                elif (cname == "Review"):
                    FileStorage.__objects[k] = models.review.Review(**v)

    def destroy(self, id_s):
        """Removes an entry from storage"""
        if (id_s in FileStorage.__objects):
            del FileStorage.__objects[id_s]
