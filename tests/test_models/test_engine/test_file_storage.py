#!/usr/bin/python3
"""Module Test file_storage"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""
    def test_filestorage(self):
        storage = FileStorage()
        my_model = FileStorage()
        my_model_dict = storage.all()
        self.assertEqual(type(my_model_dict), dict)

if __name__ == "__main__":
    unittest.main()