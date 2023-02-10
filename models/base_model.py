#!/usr/bin/python3
"""Defines all common attributes/methods for other classes."""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """Represents a class for base model of object hierachy."""


    def __init__(self), *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """Returns a string representation on the instance."""

        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with the current datetime."""

        self.updated_at = datetime.datetime.now()
        storage.save()


    def to_dict(self):
        """Returns a dict containing all keys/values of the instance."""

        dict1 = self.__dict__.copy()
        dict1['__class__'] = self.__class__.__name__
        dict1['updated_at'] = self.updated_at.isoformat()
        dict1['created_at'] = self.created_at.isoformat()
        return dict1
