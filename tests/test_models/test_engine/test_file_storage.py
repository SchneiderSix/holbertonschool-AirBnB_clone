#!/usr/bin/python3
"""Module Test file_storage"""
import unittest
import models


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""
    def test_filestorage(self):
        my_model = FileStorage()
        my_model_dict = storage.all()
        self.assertEqual(type(my_model_list), dict)

if __name__ == "__main__":
    unittest.main()