#!/usr/bin/python3
"""Module Test Class BaseModel"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing base_model"""
    def test_BaseModel_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(my_model.name, "My Fisrt Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        self.assertEqual(type(my_model_dict), dict)

class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""
    def test_filestorage(self):
        my_model = FileStorage()
        my_model_list = storage.all()
        self.assertEqual(type(my_model_list), list)

if __name__ == "__main__":
    unittest.main()
