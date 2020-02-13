#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        '''Assign the current datetime when an instance is created'''
        self.create_at = datetime.now()
        '''Give the current datetime when an object is changed'''
        self.update_at = datetime.now()

    def __str__(self):
        """String method to return prettier version of the BaseModel"""
        return ("[{}] ({}) <{}>".format(type(self).__name__, self.id,
                                        self.__dict__))
