#!/usr/bin/python3
"""
Test class State
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class tests"""

    def test_create(self):
        """creates new instance"""
        model = State()
        self.assertIsInstance(model, State)

    def test_sub_instance(self):
        """Test if it's a child of BaseModel"""
        model = State()
        self.assertIsInstance(model, BaseModel)


if __name__ == '__main__':
    unittest.main()
