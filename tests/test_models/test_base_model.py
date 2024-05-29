#!/usr/bin/python3
"""Test class for BaseModel"""
import models
import uuid
import unittest
import os
import sys
Base = models.base_model.BaseModel


class TestBestModel(unittest.TestCase):
    """TestBaseMidelClass"""

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()

    def tearDown(self):
        self.base1 = None
        self.base2 = None

    def testBaseModel(self):
        the_id = str(uuid.uuid4())
        self.assertIsInstance(the_id, str)
        self.assertTrue(len(the_id), 36)


if __name__ == "__main__":
    unittest.main()
