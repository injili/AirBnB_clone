#!/usr/bin/python3
"""
unittests for the base_model module
#run with either of the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
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
