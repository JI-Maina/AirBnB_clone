#!/usr/bin/python3
"""Defines a State module."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attribute:
        - name (str): name of the state
    """
    name = ""
