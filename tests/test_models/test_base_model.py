#!/usr/bin/python3
"""Module Test Class BaseModel"""


import unittest
from models.engine.file_storage import FileStorage
import models
from datetime import datetime


class BaseModel:
    """Class Base"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == '__class__':
                    continue
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """String expression of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates ins att with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary with keys/values of __dict__ of the instance"""
        ndic = dict(self.__dict__)
        ndic["__class__"] = self.__class__.__name__
        ndic["created_at"] = self.created_at.isoformat()
        ndic["updated_at"] = self.updated_at.isoformat()
        return ndic

class TestBaseModel(unittest.TestCase):
    """Testing base_model"""
    def test_BaseModel_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        self.assertEqual(type(my_model_dict), dict)

if __name__ == "__main__":
    unittest.main()
