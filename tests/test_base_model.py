#!/usr/bin/python3
"""
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """
    base_model = BaseModel()


    def test_save(self):
        """
        """
        pre_updated_at = TestBaseModel.base_model.updated_at
        TestBaseModel.base_model.save()
        post_updated_at = TestBaseModel.base_model.updated_at
        self.assertNotEqual(pre_updated_at, post_updated_at)

    def test_instance(self):
        self.assertIsInstance(TestBaseModel.base_model, BaseModel)

    def test_id_uniq(self):
        self.assertNotEqual(TestBaseModel.base_model.id, BaseModel().id)

    def test__str__(self):
        # self.assertEqual(TestBaseModel.base_model.__str__)
        pass

    def test_to_dict(self):
        self.assertNotEqual(TestBaseModel.base_model.to_dict(), BaseModel().__dict__)

    def test_created_at(self):
        self.assertNotEqual(TestBaseModel.base_model.created_at,
                            BaseModel().created_at)
