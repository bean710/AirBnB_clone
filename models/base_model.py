#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

    def __str__(self):
        """String method to return prettier version of the BaseModel"""
        return ("[{}] ({}) <{}>".format(type(self).__name__, self.id,
                                        self.__dict__))
