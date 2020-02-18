#!/usr/bin/python3
"""This module has tests for the console"""
import unittest
import unittest.mock
from console import HBNBCommand
from models.engine.file_storage import FileStorage
"""with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")"""

class TestConsoleClass(unittest.TestCase):
    """This is the unittest case for the console"""

    original_path = ""

    def setUp(self):
        """Resets the file storage class for each test"""
        FileStorage._FileStorage__objects = {}
        TestConsoleClass.original_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Removes test json file"""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = TestConsoleClass.original_path

    def testHelp(self):
        """Tests the help command"""
        print("Foo")
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.read())
