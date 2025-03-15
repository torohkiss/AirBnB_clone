#!/usr/bin/python3
"""BaseModel class that defines common attributes/methods for other classes"""


import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class with common attributes/methods"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
         self.updated_at = datetime.now()

    def save(self):
        """The save method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_dict
