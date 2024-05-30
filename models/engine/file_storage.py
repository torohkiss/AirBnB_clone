#!/usr/bin/python3
"""File storage class"""

import models
import json
from os.path import exists


class FileStorage:
    """The file storage class"""
    self.__file_path = "file.json"
    self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            objkey = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[objkey] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(f"{class_name}(**value)")
        except FileNotFoundError:
            pass
