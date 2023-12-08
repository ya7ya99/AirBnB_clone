#!/usr/bin/python3
"""testing the review class"""

import unittest
from models.review import Review
from datetime import datetime


class Testingreview(unittest.TestCase):
    """
    testing the class review if it exists
    with its attributes and checking its type
    """

    def test_review(self):
        thereview = Review()
        self.assertTrue(hasattr(thereview, "id"))
        self.assertTrue(hasattr(thereview, "place_id"))
        self.assertTrue(hasattr(thereview, "user_id"))
        self.assertTrue(hasattr(thereview, "text"))
        self.assertTrue(hasattr(thereview, "created_at"))
        self.assertTrue(hasattr(thereview, "updated_at"))

        self.assertIsInstance(thereview.id, str)
        self.assertIsInstance(thereview.place_id, str)
        self.assertIsInstance(thereview.user_id, str)
        self.assertIsInstance(thereview.text, str)
        self.assertIsInstance(thereview.created_at, datetime)
        self.assertIsInstance(thereview.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
