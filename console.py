#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
from models.user import User

modelClasses = ("BaseModel", "User")

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def lineignore(self):
        """Ignore empty line"""
        pass

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit at the end of file"""
        return True

    def do_create(self, line):
        """Creates a new insance of a class, saves it, then prints the ID"""
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")
            return
        if (args[0] == "BaseModel"):
            bm = BaseModel()
            bm.save()
            print(bm.id)
        elif (args[0] == "User"):
            ui = User()
            ui.save()
            print(ui.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows the string representation of an instance"""
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")
            return

        if (args[0] not in modelClasses):
            print("** class doesn't exist **")
            return

        if (len(args) == 1):
            print("** instance id missing **")
            return

        if ("{}.{}".format(args[0], args[1]) in models.storage.all().keys()):
            print (models.storage.all()["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Lists all fo the objects in storage"""
        args = line.split()
        all_vals = models.storage.all().values()

        if (len(args) == 0):
            print([str(x) for x in all_vals])
            return

        if (args[0] not in modelClasses):
            print("** class doesn't exist **")
            return

        print([str(v) for v in all_vals if v.to_dict()["__class__"] == args[0]])

    def do_destroy(self, line):
        """Removes an object from storage"""
        args = line.split()

        if (len(args) == 0):
            print("** class name missing **")
            return

        if (args[0] not in modelClasses):
            print("** class doesn't exist **")
            return

        if (len(args) == 1):
            print("** instance id missing **")
            return

        if ("{}.{}".format(args[0], args[1]) in models.storage.all().keys()):
            models.storage.destroy("{}.{}".format(args[0], args[1]))
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
