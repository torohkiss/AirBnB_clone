#!/usr/bin/python3
"""The console cmd module"""


import cmd

class HBNBCommand(cmd.Cmd):
    """The console comand interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """quits the console"""
        return True

    def do_quit(self, line):
        """also quits the console"""
        return True

    def emptyline(self):
        """an emptyline that does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
