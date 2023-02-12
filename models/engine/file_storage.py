#!/usr/bin/python3
"""Defines a class that serializes instances to JSON file
    & deserializes JSON file to instances."""

import json
from models.base_model import BaseModel
from os.path import exists


class FileStorage:
    """Represents a storage class.

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): stores all obects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (dict): dictionary representation of an instance.
        """
        name = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        my_json_dict = {}
        for key, value in FileStorage.__objects.items():
            my_json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r') as f:
                my_obj = json.load(f)
                for value in my_obj.values():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
