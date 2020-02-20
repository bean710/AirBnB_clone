#!/usr/bin/python3
"""This module contains the class to test the User class"""
import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """Class contains testing methods"""

    def testInit(self):
        """Tests that all of the class attributes are properly set up"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def testClassAttr(self):
        """Tests that the attributes are class attributes"""
        u1 = User()
        u2 = User()

        u1.email = "foo@bar.fubar"
        self.assertEqual(u1.email, "foo@bar.fubar")
        self.assertNotEqual(u2.email, "foo@bar.fubar")

        u2.first_name = "Bobby"
        self.assertEqual(u2.first_name, "Bobby")
        self.assertNotEqual(u1.first_name, "Bobby")
