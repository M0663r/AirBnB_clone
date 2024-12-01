#!/usr/bin/python3
"""
File contains code to test the BaseModel class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    BaseModel tester class
    """
    def setUp(self):
        self.test_storage = FileStorage()
        self.test_model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del self.test_storage
        del self.test_model
        if os.path.exists('file.json'):
            os.remove('file.json')
        return super().tearDown()

    def test_instance(self):
        """Test for correct instance"""
        self.assertIsInstance(self.test_storage, FileStorage)

    def test_obj_exist(self):
        """Test if object can be found"""
        self.test_storage.new(self.test_model)
        self.assertIs(self.test_storage.search(
            'BaseModel', self.test_model.id), self.test_model)

    def test_obj_not_exist(self):
        """Test if object cannot be found"""
        self.test_storage.new(self.test_model)
        self.assertRaisesRegex(Exception, 'BaseModel.*',
                self.test_storage.search, 'BaseModel', '1233456788')
