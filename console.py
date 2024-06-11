#!/usr/bin/python3
"""The console file"""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """the HBNBCommand class set up"""

    classes = {"BaseModel", "User"}

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """self.lastcmd = ""Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        model = eval(line)()
        model.save()
        print(model.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                objkey = ".".join(args)
                if objkey not in storage.all().keys():
                    print("** no instance found **")
                    return
                print(storage.all()[objkey])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            if args[1]:
                objkey = ".".join(args)
                if objkey not in storage.all().keys():
                    print("** no instance found **")
                    return
                del storage.all()[objkey]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        if len(args) == 0:
            print([str(v) for v in storage.all().values()])
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) > 0:
            print([str(v) for v in storage.all().values()
                if type(v).__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return



    def do_EOF(self, line):
        """Quits the command interpreter"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
