#!/usr/bin/python3
"""Defines an Amenity module."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        - name (str): amenity name
    """
    name = ""
