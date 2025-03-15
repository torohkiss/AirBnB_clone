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
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as file:
                    loaded_dict = json.load(file)
                    self.__objects = loaded_dict
        except Exception:
            pass

    #print(dir(FileStorage))
