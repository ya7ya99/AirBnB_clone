#!/usr/bin/python3
"""Import json and os modules."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""FileStorage class."""
class FileStorage:
    """FileStorage class."""

    __file_path = "file_v2.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        file_path = FileStorage.__file_path
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                loaded_objects = json.load(file)
            while loaded_objects:
                key, value = loaded_objects.popitem()
                class_name = value.get('__class__')
                if class_name:
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    self.new(obj)

