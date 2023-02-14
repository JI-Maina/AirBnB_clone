#!/usr/bin/python3
"""Unittests for class Place."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Place testcases."""

    def test_create_place(self):
        place = Place()

        self.assertIsInstance(place, Place)

    def test_has_methods(self):
        place = Place()

        self.assertTrue(hasattr(place, '__init__'))
        self.assertTrue(hasattr(place, '__str__'))
        self.assertTrue(hasattr(place, 'save'))
        self.assertTrue(hasattr(place, 'to_dict'))

    def test_has_attributes(self):
        place = Place()

        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
    
    def test_save_place(self):
        place = Place()
        place.save()

        self.assertNotEqual(place.created_at, place.updated_at)

    def test_set_attributes(self):
        place = Place()
        place.name = "Ndakaini"
        place.max_guests = 5
        place.price_by_night = 500

        self.assertTrue(place.name, "Ndakaini")
        self.assertTrue(place.max_guests, 5)
        self.assertTrue(place.price_by_night, 500)

if __name__ == "__main__":
    unittest.main()
