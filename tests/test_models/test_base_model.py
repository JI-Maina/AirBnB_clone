#!/usr/bin/python3
"""test BaseModel"""

import unittest
#import pep8
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test Cases for BaseModel."""

#    def test_pep8_BaseModel(self):
#        style = pep8.StyleGuide(quiet=True)
#        p = style.check_files(['models/base_model.py'])

#        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_instance_creation(self):
        mod = BaseModel()

        self.assertIsInstance(mod, BaseModel)
        self.assertEqual(type(mod), BaseModel)
        self.assertTrue(hasattr(mod, "id"))
        self.assertTrue(hasattr(mod, "created_at"))
        self.assertFalse(hasattr(mod, "update_at"))

    def test_unique_id(self):
        mod = BaseModel()
        mod1 = BaseModel()

        self.assertNotEqual(mod.id, mod1.id)

    def test_instance_save(self):
        mod = BaseModel()
        mod.save()

        key = f"{mod.__class__.__name__}.{mod.id}"
        self.assertIn(key, storage.all().keys())

    def test_to_dict(self):
        mod = BaseModel()
        md = mod.to_dict()

        self.assertEqual(mod.id, md['id'])

    def test_doc(self):
        mod = BaseModel()

        self.assertIsNotNone(mod.__doc__)

    def test_attributes(self):
        mod = BaseModel()

        self.assertTrue(mod.id)
        self.assertTrue(mod.created_at)
        self.assertTrue(mod.updated_at)

    def test_kwargs(self):
        mod = BaseModel()
        md_1 = mod.to_dict()
        md_2 = BaseModel(**md_1)

        self.assertEqual(mod.id, md_2.id)
        self.assertEqual(mod.created_at, md_2.created_at)

if __name__ == "__main__":
    unittest.main()
