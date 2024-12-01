#!/usr/bin/python3
"""
Program test BaseModel class
"""
import unittest
import os
import models
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Base class test
    """

    def setUp(self):
        self.test_model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del self.test_model
        if os.path.exists("file.json"):
            os.remove("file.json")
        models.storage.clean()
        return super().tearDown()

    def test_create_inst(self):
        """Test instance creation"""
        self.assertIsInstance(self.test_model, BaseModel)

    def test_save(self):
        """Tests the save function
        """
        self.test_model.save()

        file = 'file.json'
        with open(file, mode='r+', encoding='utf-8') as f:
            file_det = f.read()
            data = json.loads(file_det)

        self.assertTrue('{}.{}'.format(type(self.test_model).__name__,
                        self.test_model.id) in data)

        self. assertDictEqual(self.test_model.to_dict(), data['{}.{}'.format(
                            type(self.test_model).__name__,
                            self.test_model.id)])

    def test_assign_attr(self):
        """Test new attribute"""
        self.test_model.name = "ALX-Africa"
        self.test_model.my_number = 24
        self.assertIs(self.test_model.name, "ALX-Africa")
        self.assertIs(self.test_model.my_number, 24)

    def test_instance_frm_dict(self):
        """create instance from dict"""
        test_dict = {'id': '0d73ba7d-8587-42d5-8cf7-960ba82c6488',
                     'created_at': '2022-09-10T15:00:49.586560',
                     'updated_at': '2022-09-10T15:00:49.586584',
                     '__class__': 'BaseModel'}
        myModel = BaseModel(**test_dict)
        self.assertIsInstance(myModel, BaseModel)
        self.assertEqual(myModel.id, '0d73ba7d-8587-42d5-8cf7-960ba82c6488')

    def test_instance_to_dict(self):
        self.test_model.name = "ALX-Africa"
        self.test_model.my_number = 24
        my_json_model = self.test_model.to_dict()

        self.assertDictEqual(my_json_model, {
            'id': self.test_model.id,
            'created_at': self.test_model.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.test_model.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'name': self.test_model.name,
            'my_number': self.test_model.my_number,
            '__class__': BaseModel.__name__})


if __name__ == '__main__':
    unittest.main()
