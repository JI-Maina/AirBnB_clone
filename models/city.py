#!/usr/bin/python3
"""Defines a City."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city

    Attributes:
        - state_id (str): is the id of state
        - name (str): state name
    """

    state_id = ""
    name = ""
