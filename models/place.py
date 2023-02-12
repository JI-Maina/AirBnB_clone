#!/usr/bin/python3
"""Defines Place Module."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        - city_id (str): city id
        - user_id (str): user identity
        - name (str): name of place
        - description (str): short details of place
        - number_rooms (int): no. of available rooms
        - number_bathrooms (int): no. of available bathrooms
        - max_guest (int): maximum no. of visitors
        - price_by_night (int): cost of one night
        - latitude (float): area latitude
        - longitude (float): area longitude
        - amenity_ids (list): list of available amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
