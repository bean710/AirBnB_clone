#!/usr/bin/python3
"""This file defines a review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public attributes for review class"""
    place_id = ""
    user_id = ""
    text = ""
