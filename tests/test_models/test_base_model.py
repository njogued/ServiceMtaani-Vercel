#!/usr/bin/python3
"""Module that handle basemodel test cases
"""
import unittest
from models.base_model import BaseModel
from models.engine import storage
from datetime import datetime

class BaseModelTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the database
        storage.reload()
        
    def test_base_model_initialization(self):
        # Test the initialization of BaseModel with default values
        model = BaseModel()
        
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)
    
    def test_base_model_initialization_with_arguments(self):
        # Test the initialization of BaseModel with arguments
        model = BaseModel(name='John Doe', age=25)
        
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)
        self.assertEqual(model.name, 'John Doe')
        self.assertEqual(model.age, 25)
    
    def test_base_model_save(self):
        # Test saving the BaseModel instance
        model = BaseModel()
        initial_updated_at = model.updated_at
        
        model.save()
        
        self.assertNotEqual(model.updated_at, initial_updated_at)
    
    def test_base_model_delete(self):
        # Test deleting the BaseModel instance
        model = BaseModel()
        model.save()
        
        model.delete()
        saved_model = storage.get(BaseModel, model.id)
        
        self.assertIsNone(saved_model)
    
    def test_base_model_to_str(self):
        # Test the to_str method of BaseModel
        model = BaseModel(name='John Doe', age=25)
        
        expected_str = f"Class: BaseModel, ID: {model.id}, DETAILS: {{'id': '{model.id}', 'created_at': '{model.created_at.strftime('%m/%d/%Y, %H:%M:%S')}', 'updated_at': '{model.updated_at.strftime('%m/%d/%Y, %H:%M:%S')}', 'name': 'John Doe', 'age': 25}}"
        self.assertEqual(model.to_str(), expected_str)
    
    def test_base_model_str(self):
        # Test the __str__ method of BaseModel
        model = BaseModel(name='John Doe', age=25)
        
        expected_str = f"Class: BaseModel, ID: {model.id}, DETAILS: {{'id': '{model.id}', 'created_at': '{model.created_at.strftime('%m/%d/%Y, %H:%M:%S')}', 'updated_at': '{model.updated_at.strftime('%m/%d/%Y, %H:%M:%S')}', 'name': 'John Doe', 'age': 25}}"
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()

