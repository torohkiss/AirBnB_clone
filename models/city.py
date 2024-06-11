#!/usr/bin/python3
"""The city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """The city class that inherits fronm basemodel"""

    state_id = ""
    name = ""
