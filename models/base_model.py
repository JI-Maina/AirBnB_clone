#!/usr/bin/python3
"""Defines all common attributes/methods for other classes."""
import datetime
from uuid import uuid4


class BaseModel:
    """Represents a class."""
    def __init__(self):
        """Initializes an instance with attributes id, created_at & updated_at."""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation on the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()
        return self.__dict__
