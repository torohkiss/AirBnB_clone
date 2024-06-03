#!/usr/bin/python3
"""The base model class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The Basemodel class"""

    def __init__(self, *args, **kwargs):
        """initializing the base model class"""
        if kwargs:
            #for key, value in kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """to string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """to dict method"""
        adict = self.__dict__.copy()
        #adict["__class__"] = self.__class__
        adict["__class__"] = self.__class__.__name__
        adict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        adict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return adict
