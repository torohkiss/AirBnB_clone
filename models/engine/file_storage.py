#!/usr/bin/python3
"""File storage class"""

import models
import json


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
        newobj = {}
        for key, value in self.__objects.items():
            newobj[key] = value.to_dict()
        with open(self.__file_path, 'w') as the_file:
            json.dump(newobj, the_file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as the_file:
                object_dict = json.load(the_file)

            for key, val in object_dict.items():
                class_name = classes[(val['__class__'])](**val)
                self.__objects[key] = cls_name
        except FileNotFoundError:
            pass
