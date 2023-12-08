#!/usr/bin/python3
"""testing the city class"""

import unittest
from models.city import City
from datetime import datetime


class TestingCity(unittest.TestCase):
    """
    testing the class city if it exists
    with its attributes and checking its type
    """

    def test_city(self):
        thecity = City()
        self.assertTrue(hasattr(thecity, "name"))
        self.assertTrue(hasattr(thecity, "id"))
        self.assertTrue(hasattr(thecity, "state_id"))
        self.assertTrue(hasattr(thecity, "created_at"))
        self.assertTrue(hasattr(thecity, "updated_at"))

        self.assertIsInstance(thecity.name, str)
        self.assertIsInstance(thecity.id, str)
        self.assertIsInstance(thecity.state_id, str)
        self.assertIsInstance(thecity.created_at, datetime)
        self.assertIsInstance(thecity.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
