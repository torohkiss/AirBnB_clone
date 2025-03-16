#!/usr/bin/python3
import json
import os


class FileStorage:
    """The file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
            
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        try:
            from models.base_model import BaseModel
            from models.user import User
            classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    }

            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        if class_name in classes:
                            self.__objects[key] = classes[class_name](**value)
        except Exception:
            pass

    #print(dir(FileStorage))
