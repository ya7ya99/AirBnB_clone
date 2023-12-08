#!/usr/bin/python3
"""testing the class BasseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestingBaseModel(unittest.TestCase):
    """
    testing the class BaseModel if it exists with its
    methods, attributes and checking its types
    """
    def test_BaseModel(self):
        theBaseModel = BaseModel()
        self.assertTrue(hasattr(theBaseModel, "__init__"))
        self.assertTrue(hasattr(theBaseModel, "__str__"))
        self.assertTrue(hasattr(theBaseModel, "save"))
        self.assertTrue(hasattr(theBaseModel, "to_dict"))

        self.assertTrue(hasattr(theBaseModel, "id"))
        self.assertTrue(hasattr(theBaseModel, "created_at"))
        self.assertTrue(hasattr(theBaseModel, "updated_at"))

        self.assertIsInstance(theBaseModel.id, str)
        self.assertIsInstance(theBaseModel.created_at, datetime)
        self.assertIsInstance(theBaseModel.updated_at, datetime)

    def test_str(self):
        dt = datetime.now()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "1"
        bm.created_at = bm.updated_at = dt
        bmstring = bm.__str__()
        self.assertIn("[BaseModel] (1)", bmstring)
        self.assertIn("'id': '1'", bmstring)
        self.assertIn("'created_at': " + dt_repr, bmstring)
        self.assertIn("'updated_at': " + dt_repr, bmstring)

    def test_to_dict(self):
        dt = datetime.now()
        bm = BaseModel()
        bm.id = "1"
        bm.created_at = bm.updated_at = dt
        bmdictionary = bm.to_dict()
        bmdict1 = "{'__class__': 'BaseModel', 'id': '1', 'created_at': "
        bmdict2 = f"'{dt.isoformat()}', 'updated_at': '{dt.isoformat()}'"
        self.assertIsInstance(bmdictionary, dict)
        bmdictionary = str(bm.to_dict())
        self.assertIn(bmdict1, bmdictionary)
        self.assertIn(bmdict2, bmdictionary)

    def test_save(self):
        with open("file.json", "w") as file:
            file.write('{}')
        dt = datetime.now()
        bm = BaseModel()
        bm.id = "1"
        bm.created_at = bm.updated_at = dt
        bm.save()
        with open("file.json", "r") as file:
            data = file.read()
        data = str(data)
        bmdict1 = '"BaseModel.1"'
        bmdict2 = '"id": "1"'
        self.assertIn(bmdict1, data)
        self.assertIn(bmdict2, data)


if __name__ == "__main__":
    unittest.main()
