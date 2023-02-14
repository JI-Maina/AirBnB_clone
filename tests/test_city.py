#!/usr/bin/python3
""" Test city """

import unittest
#import pep8
from models.city import City

class Test_City(unittest.TestCase):
    """ Tests city """

#    def test_pep8_City(self):
#        """Tests pep8 style"""
#        style = pep8.StyleGuide(quiet=True)
#        p = style.check_files(['models/city.py'])
#        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_city_has_attributes(self):
        city = City()

        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_set_attribute(self):
        city = City()
        city.state_id = 501
        city.name = "Nairobi"

        self.assertTrue(city.state_id, 501)
        self.assertTrue(city.name, "Nairobi")

    def test_save_City(self):
        city = City()
        city.save()

        self.assertNotEqual(city.created_at, city.updated_at)

    def test_inst(self):
        city = City()

        self.assertIsInstance(city, City)

if __name__ == "__main__":
   unittest.main()
