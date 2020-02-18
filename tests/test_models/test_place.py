"""Module for testing the Base class"""
import unittest
import time
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Tests the place class"""

    def testName(self):
        """Tests the name attribute"""
        self.assertIs(type(Place.name), str)

    def testCityId(self):
        """Tests the city id attribute"""
        self.assertIs(type(Place.city_id), str)

    def testUserId(self):
        """Tests the user id attribute"""
        self.assertIs(type(Place.user_id), str)

    def testDescription(self):
        """Tests the description attribute"""
        self.assertIs(type(Place.description), str)

    def testNumberRooms(self):
        """Tests the number_rooms attribute"""
        self.assertIs(type(Place.number_rooms), int)

    def testNumberBathrooms(self):
        """Tests the number_bathrooms attribute"""
        self.assertIs(type(Place.number_bathrooms), int)

    def testMaxGuest(self):
        """Tests the max_guest attribute"""
        self.assertIs(type(Place.max_guest), int)

    def testPriceByNight(self):
        """Tests the price_by_night attribute"""
        self.assertIs(type(Place.price_by_night), int)

    def testLatitude(self):
        """Tests the latutude attribute"""
        self.assertIs(type(Place.latitude), float)

    def testLongitude(self):
        """Tests the longitude attribute"""
        self.assertIs(type(Place.longitude), float)

    def testAmenityIds(self):
        """Tests the amenity_ids attribute"""
        self.assertIs(type(Place.amenity_ids), list)
        self.assertIs(type(Place.amenity_ids[0]), str)
