#!/usr/bin/env python3
"""This module has the command prompt class"""
import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

modelClasses = ("BaseModel", "User", "Place", "State", "City", "Amenity",
                "Review")


class HBNBCommand(cmd.Cmd):
    """Class to define how the command prompt interacts with the program"""
    prompt = "(hbnb) "

    def emptyline(self):
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
        if (args[0] in modelClasses):
            bm = eval(args[0] + "()")
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def complete_create(self, text, line, begidx, endidx):
        """Text completion for create command"""
        return [i for i in modelClasses if i.startswith(text)]

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
            print(models.storage.all()["{}.{}".format(args[0], args[1])])
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

        print([str(v) for v in all_vals
               if v.to_dict()["__class__"] == args[0]])

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

    def do_update(self, line):
        """Updates an instance in storage"""
        args = re.compile(r"(\"[^\"]+\"|[^,\s]+)").findall(line)
        s_all = models.storage.all()

        args = [x.strip("\"") for x in args]

        if (len(args) == 0):
            print("** class name missing **")
            return

        if (args[0] not in modelClasses):
            print("** class doesn't exist **")
            return

        if (len(args) == 1):
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if (key not in s_all.keys()):
            print("** no instance found **")
            return

        if (len(args) == 2):
            print("** attribute name missing **")
            return

        if (len(args) == 3):
            print("** value missing **")
            return

        s_all[key].__dict__[args[2]] = args[3]
        s_all[key].save()

    def default(self, line):
        """Handles custom format commands"""
        if (re.match(r"\w+\.\w+(\(\)|\(\"[^\"]*\"(?:, (\"[^\"]*\"|{.*}))*\))",
                     line) is None):
            super().default(line)
            return

        s_all = models.storage.all()

        cname = line.split(".")[0]
        command = line.split(".")[1].split("(")[0]
        arg = line.split("(")[1][:-1]

        if (command == "all"):
            if (cname not in modelClasses):
                print("** class doesn't exist **")
                return

            self.do_all(cname)
        elif (command == "count"):
            if (cname not in modelClasses):
                print("** class doesn't exist **")
                return

            count = sum(1 for k, v in s_all.items()
                        if v.to_dict()["__class__"] == cname)
            print(count)
        elif (command == "show"):
            if (cname not in modelClasses):
                print("** class doesn't exist **")
                return

            if (len(arg) <= 2):
                print("** no instance found **")
                return

            arg = arg[1:-1]

            if ("{}.{}".format(cname, arg) in models.storage.all().keys()):
                print(models.storage.all()["{}.{}".format(cname, arg)])
            else:
                print("** no instance found **")
        elif (command == "destroy"):
            if (cname not in modelClasses):
                print("** class doesn't exist **")
                return

            self.do_destroy(cname + " " + arg[1:-1])
        elif (command == "update"):
            self.do_update(cname + " " + arg)
        else:
            super().default(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
