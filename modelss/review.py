#!/usr/bin/python3
"""The review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The review class that inherits from basemodel"""

    place_id = ""
    user_id = ""
    text = ""
