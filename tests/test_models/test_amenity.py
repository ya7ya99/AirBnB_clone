#!/usr/bin/python3
"""testing theamenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestingAmenity(unittest.TestCase):
    """
    testing the class amenity if it exists
    with its attributes and checking its type
    """

    def testamenity(self):
        theamenity = Amenity()
        self.assertTrue(hasattr(theamenity, "name"))
        self.assertTrue(hasattr(theamenity, "id"))
        self.assertTrue(hasattr(theamenity, "created_at"))
        self.assertTrue(hasattr(theamenity, "updated_at"))

        self.assertIsInstance(theamenity.name, str)
        self.assertIsInstance(theamenity.id, str)
        self.assertIsInstance(theamenity.created_at, datetime)
        self.assertIsInstance(theamenity.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
