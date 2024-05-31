#!/usr/bin/python3
"""File storage class"""

#import models
from models.base_model import BaseModel
import json
import os.path


class FileStorage:
    """The file storage class"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary obj"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            objkey = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[objkey] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                objdicts = json.load(f)

            my_obj = {}
            for key, value in objdicts.items():
                cls_name = value['__class__']
                my_obj[key]= eval(cls_name)(**value)
            self.__objects.update(my_obj)
