#!usr/bin/python3
"""Unit tests for class State."""

from models.state import State
#import pep8
import unittest


class TestState(unittest.TestCase):
    """Test state creation and state methods."""

    def test_create_state(self):
        state = State()

        self.assertIsInstance(state, State)

    def test_has_methods(self):
        state = State()

        self.assertTrue(hasattr(state, '__str__'))
        self.assertTrue(hasattr(state, '__init__'))
        self.assertTrue(hasattr(state, 'to_dict'))
        self.assertTrue(hasattr(state, 'save'))

    def test_has_attribute(self):
        state = State()

        self.assertTrue(hasattr(state, 'name'))

    def test_set_attributes(self):
        state = State()
        state.name = "Kenya"
        
        self.assertEqual(state.name, 'Kenya')

    def test_state_to_dict(self):
        state = State()
        state.name = "Kenya"
        state_dict = state.to_dict()

        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('id', state_dict)
        self.assertIn('name', state_dict)
        self.assertIn('__class__', state_dict)

    def test_save_state(self):
        state = State()
        state.save()

        self.assertNotEqual(state.created_at, state.updated_at)

if __name__ == "__main__":
    unittest.main()
