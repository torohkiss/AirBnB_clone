#!/usr/bin/python3
"""The console cmd module"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The console comand interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """creates a class instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        available_classes = {
                'BaseModel': BaseModel,
                }

        if class_name not in available_classes:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints string rep of an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name == "BaseModel":
            new_instance = BaseModel()
        else:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objects:
            print("** no instance found **")
        else:
            instance = all_objects[key]
            print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and  (save the change into the JSON file)"""

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objects:
            print("** no instance found **")
            return
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = line.split()
        all_objects = storage.all()
        result = []

        if len(args) == 0:
            for obj in all_objects.values():
                result.append(str(obj))
            print(result)
            return

        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return

        for key, obj in all_objects.items():
            if key.split('.')[0] == class_name:
                result.append(str(obj))
        print(result)
        return
    
    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)."""

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        obj = all_objects[key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_name in ["id", "created_at", "updated_at"]:
            return
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        setattr(obj, attr_name, attr_value)
        storage.save()

        

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
