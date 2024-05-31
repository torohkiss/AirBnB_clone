#!/usr/bin/python3
"""Test class for BaseModel"""
import json
import unittest
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBestModel(unittest.TestCase):
    """TestBaseMidelClass"""

    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        del self.base1
        del self.base2

    def test_BaseModel(self):
        the_id = str(uuid.uuid4())
        self.assertIsInstance(the_id, str)
        self.assertTrue(len(the_id), 36)




if __name__ == "__main__":
    unittest.main()
