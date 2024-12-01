#!/usr/bin/python3
"""
Test class review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class tests"""

    def test_create(self):
        """creates new instance"""
        model = Review()
        self.assertIsInstance(model, Review)

    def test_sub_instance(self):
        """Test if it's a child of BaseModel"""
        model = Review()
        self.assertIsInstance(model, BaseModel)


if __name__ == '__main__':
    unittest.main()
