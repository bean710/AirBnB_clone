#!/usr/bin/python3
"""This module is to define a place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Public attributes for Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
