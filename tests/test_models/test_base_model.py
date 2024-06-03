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
        """setup method"""
        self.base1 = BaseModel()

    def tearDown(self):
        """tears things down yo"""
        del self.base1

    def test_BaseModel(self):
        """testing the uuid"""
        the_id = str(uuid.uuid4())
        self.assertIsInstance(the_id, str)
        self.assertTrue(len(the_id), 36)

    def test_instance_creation(self):
        """testing instances created"""
        self.assertIsInstance(self.base1, BaseModel)
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base1.updated_at, datetime)

    def test_string_representation(self):
        """testing the string created and returned"""
        self.base1.name = "My First Model"
        self.base1.my_number = 89
        str_representation = str(self.base1)
        self.assertIn(self.base1.id, str_representation)
        self.assertIn("name", str_representation)
        self.assertIn("my_number", str_representation)

    def test_save(self):
        """testing the save method"""
        created_at = self.base1.created_at
        updated_at = self.base1.updated_at
        self.base1.save()
        self.assertGreater(self.base1.updated_at, updated_at)
        self.assertEqual(self.base1.created_at, created_at)

    def test_to_dict_method(self):
        """testing the to dict mthod"""
        self.base1.name = "My First Model"
        self.base1.my_number = 89
        base1__json = self.base1.to_dict()
        self.assertIsInstance(base1__json, dict)
        self.assertIn("__class__", base1__json)
        self.assertEqual(base1__json["__class__"], 'BaseModel')
        self.assertIn("id", base1__json)
        self.assertIn("created_at", base1__json)
        self.assertIn("updated_at", base1__json)
        self.assertEqual(base1__json["created_at"], self.base1.created_at.isoformat())
        self.assertEqual(base1__json["updated_at"], self.base1.updated_at.isoformat())


        




if __name__ == "__main__":
    unittest.main()
