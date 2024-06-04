#!/usr/bin/python3
"""The console file"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the HBNBCommand class set up"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """Quits the command interpreter"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
