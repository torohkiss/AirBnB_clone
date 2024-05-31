#!/usr/bin/python3
"""File storage class"""

#import models
from models.base_model import BaseModel
"""
import json
import os.path


class FileStorage:
    """The file storage class"""
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
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                objdicts = json.load(f)

            my_obj = {}
            for key, value in objdicts.items():
                cls_name = value['__class__']
                my_obj[key]= eval(cls_name)(**value)
            self.__objects.update(my_obj)
"""
import json
from os.path import exists

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
         """Deserializes the JSON file to __objects"""
         if exists(self.__file_path):
             with open(self.__file_path, "r") as file:
                 obj_dict = json.load(file)
                 for key, value in obj_dict.items():
                     module, class_name = key.split(".")
                     created_class = __import__(f"models.{module}", fromlist=[class_name])
                     self.__objects[key] = getattr(created_class, class_name)(**value)
