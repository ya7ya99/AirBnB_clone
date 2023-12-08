#!/usr/bin/python3
"""testing the place class"""

import unittest
from models.place import Place
from datetime import datetime


class TestingPlace(unittest.TestCase):
    """
    testing the class place if it exists
    with its attributes and checking its type
    """

    def test_place(self):
        theplace = Place()
        self.assertTrue(hasattr(theplace, "city_id"))
        self.assertTrue(hasattr(theplace, "user_id"))
        self.assertTrue(hasattr(theplace, "name"))
        self.assertTrue(hasattr(theplace, "id"))
        self.assertTrue(hasattr(theplace, "description"))
        self.assertTrue(hasattr(theplace, "number_rooms"))
        self.assertTrue(hasattr(theplace, "number_bathrooms"))
        self.assertTrue(hasattr(theplace, "max_guest"))
        self.assertTrue(hasattr(theplace, "price_by_night"))
        self.assertTrue(hasattr(theplace, "latitude"))
        self.assertTrue(hasattr(theplace, "longitude"))
        self.assertTrue(hasattr(theplace, "amenity_ids"))
        self.assertTrue(hasattr(theplace, "created_at"))
        self.assertTrue(hasattr(theplace, "updated_at"))

        self.assertIsInstance(theplace.city_id, str)
        self.assertIsInstance(theplace.user_id, str)
        self.assertIsInstance(theplace.name, str)
        self.assertIsInstance(theplace.id, str)
        self.assertIsInstance(theplace.description, str)
        self.assertIsInstance(theplace.number_rooms, int)
        self.assertIsInstance(theplace.number_bathrooms, int)
        self.assertIsInstance(theplace.max_guest, int)
        self.assertIsInstance(theplace.price_by_night, int)
        self.assertIsInstance(theplace.latitude, float)
        self.assertIsInstance(theplace.longitude, float)
        self.assertIsInstance(theplace.amenity_ids, list)
        self.assertIsInstance(theplace.created_at, datetime)
        self.assertIsInstance(theplace.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
