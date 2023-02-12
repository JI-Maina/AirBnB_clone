#!/usr/bin/python3
"""Defines a User model."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user.

    Attributes:
        - email (str): user's mail
        - password (str): user's secret key
        - first_name (str): user's first name
        - last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
