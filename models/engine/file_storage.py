#!/usr/bin/python3
"""File storage class"""

import models
import json
from os.path import exists


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
        """
        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(f"{class_name}(**value)")
        except FileNotFoundError:
            pass
            """
            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = classes[(value['__class__'])](**value)
                    self.__objects[key] = cls_name
            except FileNotFoundError:
                pass
