#!/usr/bin/python3
"""testing the user class"""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class Testinguser(unittest.TestCase):
    """
    testing the class user if it exists
    with its attributes and checking its type
    """

    def test_user(self):
        theuser = User()
        self.assertTrue(hasattr(theuser, "email"))
        self.assertTrue(hasattr(theuser, "password"))
        self.assertTrue(hasattr(theuser, "first_name"))
        self.assertTrue(hasattr(theuser, "last_name"))
        self.assertTrue(hasattr(theuser, "id"))
        self.assertTrue(hasattr(theuser, "created_at"))
        self.assertTrue(hasattr(theuser, "updated_at"))

        self.assertIsInstance(theuser.email, str)
        self.assertIsInstance(theuser.password, str)
        self.assertIsInstance(theuser.first_name, str)
        self.assertIsInstance(theuser.last_name, str)
        self.assertIsInstance(theuser.id, str)
        self.assertIsInstance(theuser.created_at, datetime)
        self.assertIsInstance(theuser.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
