#!/usr/bin/python3
"""The user class"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """The user class defined"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
