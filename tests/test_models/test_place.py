#!/usr/bin/python3
"""
Test class Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Class tests"""

    def test_create(self):
        """creates new instance"""
        model = Place()
        self.assertIsInstance(model, Place)

    def test_sub_instance(self):
        """Test if it's a child of BaseModel"""
        model = Place()
        self.assertIsInstance(model, BaseModel)


if __name__ == '__main__':
    unittest.main()
