#!/usr/bin/python3
"""File storage class"""

import models
import json
from os.path import exists


class FileStorage:
    """The file storage class"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            objkey = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[objkey] = obj

    def save(self):
        with open(self.__file_path, 'w') as the_file:
            json.dump(self.__objects, the_file)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                module = __import__(f"models.{class_name.lower()}", fromlist=[class_name])
                cls = getattr(module, class_name)
                self.__objects[key] = cls(**value)
