#!/usr/bin/python3
"""
Script defines all common attributes/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Class defines model common to every other classes
    to be used in this project
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the class

        Args:
            args - lists of values
            kwargs - dictionary of values
        """

        if kwargs:
            for key, arg in kwargs.items():
                if key != '__class__':
                    setattr(self, key, arg)
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        changes print format for the class

        Returns:
            special class printout format
        """
        return "[{}] ({}) {}".format(
                                           type(self).__name__,
                                           self.id,
                                           self.__dict__)

    def name(self, value):
        """Assign name to the class instance
        Args:
            value (string) - name
        """
        self.name = value

    def my_number(self, value):
        """Assign number to the class instance

        Args:
            value (string) - name
        """
        self.my_number = value

    def save(self):
        """Save the object instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts instance to a dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
