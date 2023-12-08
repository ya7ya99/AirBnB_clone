#!/usr/bin/python3
"""testing the state class"""

import unittest
from models.state import State
from datetime import datetime


class TestingState(unittest.TestCase):
    """
    testing the class state if it exists
    with its attributes and checking its type
    """

    def test_state(self):
        thestate = State()
        self.assertTrue(hasattr(thestate, "name"))
        self.assertTrue(hasattr(thestate, "id"))
        self.assertTrue(hasattr(thestate, "created_at"))
        self.assertTrue(hasattr(thestate, "updated_at"))

        self.assertIsInstance(thestate.name, str)
        self.assertIsInstance(thestate.id, str)
        self.assertIsInstance(thestate.created_at, datetime)
        self.assertIsInstance(thestate.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
