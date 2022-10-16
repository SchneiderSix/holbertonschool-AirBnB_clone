#!/usr/bin/python3
"""Module Test Class BaseModel"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Testing base_model"""
    def test_BaseModel_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        storage = FileStorage()
        storage.all().clear()
        sve = BaseModel()
        try:
            os.remove("file.json")
        except Exception:
            pass
        sve.save()
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        self.assertEqual(type(my_model_dict), dict)
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
