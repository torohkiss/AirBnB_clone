#!/usr/bin/python3
"""Tests the file storage class"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFilestorage(unittest.TestCase):
    """The file storage class tests"""

    def setUp(self):
        """the setup metghod"""
        self.base1 = BaseModel()
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """the tear down method"""
        del self.base1
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """testing the all method"""
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)
        #self.assertEqual(len(all_objs), 0)

    def test_new(self):
        """testing the new method"""
        storage.new(self.base1)
        all_objs = storage.all()
        key = f"{self.base1.__class__.__name__}.{self.base1.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], self.base1)

    def test_save(self):
        """testing the save method"""
        self.base1.name = "My_First_Model"
        self.base1.my_number = 89
        storage.new(self.base1)
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            obj_dict = json.load(f)
        key = f"{self.base1.__class__.__name__}.{self.base1.id}"
        self.assertIn(key, obj_dict)
        self.assertEqual(obj_dict[key]["name"], "My_First_Model")
        self.assertEqual(obj_dict[key]["my_number"], 89)

    def test_reload(self):
        """thesting the reload method"""
        self.base1.name = "My_First_Model"
        self.base1.my_number = 89
        storage.new(self.base1)
        storage.save()
        storage.reload()
        all_objs = storage.all()
        key = f"{self.base1.__class__.__name__}.{self.base1.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].name, "My_First_Model")
        self.assertEqual(all_objs[key].my_number, 89)


if __name__ == '__main__':
    unittest.main()
