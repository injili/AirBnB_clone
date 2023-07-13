#!/usr/bin/python3
"""
unittests for the base_model module
#run with either of the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
from datetime import datetime
BaseModel = base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    """
    All the tests on the class BaseModel
    """

    def test_class(self):
        """
        test the functionality of the class
        """
        self.assertTrue(type(BaseModel()), BaseModel)

    def test_attributes(self):
        """
        test the public instance attributes
        """
        r1.BaseModel()
        ri.name = "Skito"
        r1.my_number = 99
        self.assertEqual(r1.name == "Skito")
        self.assertEqual(r1.my_number == 99)
        self.assertIsInstance(r1.created_at, datetime)
        self.assertLessEqual(r1.created_at, datetime.now())
        self.assertGreaterEqual(r1.created_at, datetime(2020, 1, 1))
        self.assertIsInstance(r1.updated_at, datetime)
        self.assertGreaterEqual(r1.updated_at, datetime(2020, 1, 1))
