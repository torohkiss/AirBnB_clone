#!/usr/bin/python3
"""File storage class"""

from models.base_model import BaseModel
from models.user import User
import json
import os.path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    __our_classes = {
            "BaseModel": BaseModel,
            }

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        instance_id = obj.id

        key = f"{class_name}.{instance_id}"
        self.__objects[key] = obj

    def save(self):
        temp_dict = {}

        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()

        with open(self.__file_path, encoding='utf-8', mode="w") as f:
            json.dump(temp_dict, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, encoding='utf-8', mode="r") as f:
                my_obj = json.load(f)
                
            for key, value in my_obj.items():
                class_name = value['__class__']
                #self.__objects[key] = globals()[class_name](**value)
                self.__objects[key] = self.__our_classes[class_name](**value)
                
        except FileNotFoundError:
            pass


        

"""
class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            objkey = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[objkey] = obj

    def save(self):
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, encoding='utf-8', mode='w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, encoding="utf-8",  mode="r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(f"{class_name}(**value)")
        except FileNotFoundError:
            pass
        """
