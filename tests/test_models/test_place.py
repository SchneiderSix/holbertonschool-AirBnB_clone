#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing place"""
    def test_userclass(self):
        my_model = Place()
        self.assertTrue(type(self.my_model.name) is str)

if __name__ == "__main__":
    unittest.main()
