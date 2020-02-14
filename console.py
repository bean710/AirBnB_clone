#!/usr/bin/python3

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
