#!/usr/bin/python3
"""
Program manages file storage and parsing
"""
from json import dumps, loads
from datetime import datetime


class FileStorage:
    """File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns: all available objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new obj
        Args:
            obj (object) - object details
        """
        cls_name = type(obj).__name__ + "." + obj.__dict__['id']
        FileStorage.__objects[cls_name] = obj

    def clean(self):
        """Clears object"""
        FileStorage.__objects.clear()

    def search(self, obj, obj_id):
        """Returns obj if found"""
        return self.__objects["{}.{}".format(obj, obj_id)]

    def save(self):
        """Updates object to file storage"""
        temp_obj = {}
        for key, value in self.__objects.items():
            temp_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            f.write(dumps(temp_obj))

    def reload(self):
        """Loads object from file"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                FileStorage.__objects =\
                        FileStorage.datetime_encoder(loads(f.read()))
        except Exception:
            pass

    @staticmethod
    def datetime_encoder(objs):
        """Converts dictionary details to appropriate object
        Args:
            objs (dict) - object detials"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        cls_names = {"BaseModel": BaseModel,
                     "User": User, "Place": Place,
                     "State": State, "City": City,
                     "Amenity": Amenity, "Review": Review}
        for key, value in objs.items():
            objs[key] = cls_names[value["__class__"]](**value)
        return objs
