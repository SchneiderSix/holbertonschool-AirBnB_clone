#!/usr/bin/python3
"""Module Test Class BaseModel"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing base_model"""
    def test_BaseModel_save(self):
        bm = BaseModel()
        bm.name = "My First Model"
        bm.my_number = 89
        bm.save()
        bm_dict = bm.to_dict()
        self.assertEqual(bm.__class__.__name__, "BaseModel")
        self.assertEqual(bm.name, "My First Model")
        self.assertEqual(bm.my_number, 89)
        self.assertTrue(isinstance(bm.created_at, datetime))
        self.assertTrue(isinstance(bm.updated_at, datetime))
        self.assertEqual(type(bm_dict), dict)

if __name__ == "__main__":
    unittest.main()
