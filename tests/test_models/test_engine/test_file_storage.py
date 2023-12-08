#!/usr/bin/python3
"""testing the FileStorage class"""

import unittest
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestingFileStorage(unittest.TestCase):
    """
    testing the class FileStorage if it exists
    with its attributes and checking its type
    """
    def test_reload_empty(self):
        with open("file.json", "w") as file:
            file.write('{}')
        models.storage.reload()
        self.assertNotEqual({}, models.storage.all())

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_type(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage(self):
        theFileStorage = FileStorage()
        self.assertTrue(hasattr(theFileStorage, "all"))
        self.assertTrue(hasattr(theFileStorage, "new"))
        self.assertTrue(hasattr(theFileStorage, "save"))
        self.assertTrue(hasattr(theFileStorage, "reload"))

    def test_objects(self):
        fs = FileStorage()
        objects = FileStorage._FileStorage__objects
        self.assertIsInstance(objects, dict)
        self.assertTrue(hasattr(fs, '_FileStorage__objects'))

    def test_file_path(self):
        fs = FileStorage()
        file_path = FileStorage._FileStorage__file_path
        self.assertIsInstance(file_path, str)
        self.assertTrue(hasattr(fs, '_FileStorage__file_path'))

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_save(self):
        obj_base = BaseModel()
        obj_User = User()
        obj_city = City()
        obj_state = State()
        obj_review = Review()
        obj_place = Place()
        obj_amenity = Amenity()
        models.storage.new(obj_base)
        models.storage.new(obj_User)
        models.storage.new(obj_state)
        models.storage.new(obj_place)
        models.storage.new(obj_amenity)
        models.storage.new(obj_review)
        models.storage.new(obj_city)
        models.storage.save()
        with open("file.json", "r") as file:
            data = file.read()
        self.assertIn(f"BaseModel.{obj_base.id}", data)
        self.assertIn(f"User.{obj_User.id}", data)
        self.assertIn(f"State.{obj_state.id}", data)
        self.assertIn(f"Amenity.{obj_amenity.id}", data)
        self.assertIn(f"City.{obj_city.id}", data)
        self.assertIn(f"Review.{obj_review.id}", data)
        self.assertIn(f"Place.{obj_place.id}", data)

    def test_reload(self):
        obj_base = BaseModel()
        obj_User = User()
        obj_city = City()
        obj_state = State()
        obj_review = Review()
        obj_place = Place()
        obj_amenity = Amenity()
        models.storage.new(obj_base)
        models.storage.new(obj_User)
        models.storage.new(obj_state)
        models.storage.new(obj_place)
        models.storage.new(obj_amenity)
        models.storage.new(obj_review)
        models.storage.new(obj_city)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{obj_base.id}", objs)
        self.assertIn(f"User.{obj_User.id}", objs)
        self.assertIn(f"State.{obj_state.id}", objs)
        self.assertIn(f"Amenity.{obj_amenity.id}", objs)
        self.assertIn(f"City.{obj_city.id}", objs)
        self.assertIn(f"Review.{obj_review.id}", objs)
        self.assertIn(f"Place.{obj_place.id}", objs)

    def test_reload_existence(self):
        """checking if a file doesn't exist"""
        models.storage.__FileStorage__file_path = "no_file.json"
        models.storage.reload()
        self.assertNotEqual({}, models.storage.all())


if __name__ == "__main__":
    unittest.main()
