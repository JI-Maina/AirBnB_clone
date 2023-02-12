#!/usr/bin/python3
"""Defines Review module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        - place_id (str): string comment on the place
        - user_id (str): user identity
        - text (str): comment
    """

    place_id = ""
    user_id = ""
    text = ""
