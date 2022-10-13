#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing review"""
    def test_userclass(self):
        my_model = Review()
        self.assertTrue(type(self.my_model.text) is str)

if __name__ == "__main__":
    unittest.main()
