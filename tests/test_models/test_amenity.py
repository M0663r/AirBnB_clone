#!/usr/bin/python3
"""
Test class Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class tests"""

    def test_create(self):
        """creates new instance"""
        model = Amenity()
        self.assertIsInstance(model, Amenity)

    def test_sub_instance(self):
        """Test if it's a child of BaseModel"""
        model = Amenity()
        self.assertIsInstance(model, BaseModel)


if __name__ == '__main__':
    unittest.main()
