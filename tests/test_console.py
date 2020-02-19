#!/usr/bin/python3
"""This module has tests for the console"""
import unittest
import unittest.mock
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.user import User


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
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.getvalue())

    def testBlank(self):
        """Tests that a blank line does nothing"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue())

    def testHelpQuit(self):
        """Tests that there is help documentation for quit"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertNotEqual(f.getvalue(), "")

    def testCreateOutput(self):
        """Tests that create outputs a valid ID"""
        rs = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue()[:-1], rs)

    def testCreateBaseModel(self):
        """Tests that a base model is created"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("BaseModel." + f.getvalue()[:-1],
                          models.storage.all().keys())

    def testCreateNoClass(self):
        """Tests the create command with no class given"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class name missing **")

    def testCreateWrongClass(self):
        """Tests for the correct output with an invalid class"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create EndlessSuffering")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class doesn't exist **")

    def testShowBaseModel(self):
        """Tests that a BaseModel can be shown"""
        b1 = BaseModel()

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(b1.id))
            self.assertEqual(f.getvalue().rstrip(), str(b1))

    def testShowNoClass(self):
        """Tests the show command with no class argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class name missing **")

    def testShowWrongClass(self):
        """Tests for the correct output with an invalid class"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show EndlessSuffering")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class doesn't exist **")

    def testShowNoId(self):
        """Tests for the correct output with no id argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().rstrip(),
                             "** instance id missing **")

    def testShowWrongId(self):
        """Tests for the correct output with an invalid id"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel fooBar")
            self.assertEqual(f.getvalue().rstrip(),
                             "** no instance found **")

    def testDestroyBaseModel(self):
        """Tests that the destroy command can remove a BaseModel"""
        b1 = BaseModel()

        self.assertIn("BaseModel.{}".format(b1.id),
                      models.storage.all().keys())

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(b1.id))

        self.assertNotIn("BaseModel.{}".format(b1.id),
                         models.storage.all().keys())

    def testDestroyNoClass(self):
        """Tests the destroy command with no class argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class name missing **")

    def testDestroyWrongClass(self):
        """Tests the destroy command with an invalid class"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy FooBar")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class doesn't exist **")

    def testDestroyNoId(self):
        """Tests the destroy command with no id argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().rstrip(),
                             "** instance id missing **")

    def testDestroyWrongId(self):
        """Tests the destroy command with an incorrect id"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel foobar")
            self.assertEqual(f.getvalue().rstrip(),
                             "** no instance found **")

    def testAll(self):
        """Tests the all command with no arguents"""
        self.maxDiff = None
        b1 = BaseModel()

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().rstrip(),
                             "[\"{}\"]".format(str(b1)))

    def testAllWithClass(self):
        """Tests the all command with a class argument"""
        self.maxDiff = None
        b1 = BaseModel()
        u1 = User()

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().rstrip(),
                             "[\"{}\"]".format(str(b1)))

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue().rstrip(),
                             "[\"{}\"]".format(str(u1)))

    def testAllWrongClass(self):
        """Tests the all command with an invalid class argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all FooBar")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class doesn't exist **")

    def testUpdateBaseModel(self):
        """Tests the update command"""
        b1 = BaseModel()
        b1.first_name = "foo"

        self.assertEqual(b1.first_name, "foo")
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} first_name\
                                 \"bar\"".format(b1.id))

        self.assertEqual(b1.first_name, "bar")

    def testUpdateNoClass(self):
        """Tests the update command with no class argument"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class name missing **")

    def testUpdateWrongClass(self):
        """Tests the update command with an invalid class"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update FooBar")
            self.assertEqual(f.getvalue().rstrip(),
                             "** class doesn't exist **")

    def testUpdateNoId(self):
        """Tests the update command with no id"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().rstrip(),
                             "** instance id missing **")

    def testUpdateWrongId(self):
        """Tests the update command with an invalid id"""
        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel foo123")
            self.assertEqual(f.getvalue().rstrip(),
                             "** no instance found **")

    def testUpdateNoAttr(self):
        """Tests the update command with no attribute name"""
        b1 = BaseModel()

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format(b1.id))
            self.assertEqual(f.getvalue().rstrip(),
                             "** attribute name missing **")

    def testUpdateNoValue(self):
        """Tests the update command with no value"""
        b1 = BaseModel()

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} first_name"
                                 .format(b1.id))
            self.assertEqual(f.getvalue().rstrip(),
                             "** value missing **")

    def testUpdateExtraData(self):
        """Tests the update command with extra arguments"""
        b1 = BaseModel()
        b1.first_name = "Ben"
        b1.last_name = "Keener"

        with unittest.mock.patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} first_name \"Drew\"\
                                 last_name \"foo\"".format(b1.id))
            self.assertEqual(f.getvalue().rstrip(), "")

        self.assertEqual(b1.first_name, "Drew")
        self.assertEqual(b1.last_name, "Keener")
