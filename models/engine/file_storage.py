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
        with open(self.__file_path, 'w') as the_file:
            json.dump(self.__objects, the_file)

    def reload(self):
        with open(self.__file_path, "r", encoding="utf-8") as the_file:
            self.__objects = json.load(the_file)
        objCollection = []
        newData = self.__objects.copy()
        for key in newData:
            className, id = key.split('.')
            value = self.__objects[key]

        objCollection.append(self.classes[className](**value))
        return objCollection
