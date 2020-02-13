#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, id):
        self.id = str(uuid.uuid4())
