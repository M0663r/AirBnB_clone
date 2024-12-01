#!/usr/bin/python3
"""
Test class Class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Class tests"""

    def setUp(self):
        """Runs on test init"""
        self.city = City()
        return super().setUp()

    def tearDown(self):
        """Runs on test stop"""
        del self.city
        return super().tearDown()

    def test_create(self):
        """creates new instance"""
        self.assertIsInstance(self.city, City)

    def test_sub_instance(self):
        """Test if it's a child of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_class_attr(self):
        """Class attr if it works"""
        self.city.name = 'Ilara-mokin'
        self.assertIs(self.city.name, 'Ilara-mokin')


if __name__ == '__main__':
    unittest.main()
