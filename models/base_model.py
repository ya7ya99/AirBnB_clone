#!/usr/bin/python3
"""Import necessary modules."""
from uuid import uuid4
from datetime import datetime
import models

"""BaseModel class."""
class BaseModel:
    """BaseModel class."""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance.
        Args:
            id (str(uuid)): id of the new instance
        """
        if args and len(args) > 0:
            pass  # Placeholder for handling additional args if needed
        if not kwargs:
            # If no kwargs provided, initialize with default values
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            # Handle kwargs, converting datetime strings to datetime objects
            while kwargs:
                key, value = kwargs.popitem()
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """Return a formatted string representation."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        result_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            result_dict[key] = value
        return result_dict
        
    def count(self):
        """Return the number of instances for the class."""
        objects = FileStorage._FileStorage__objects
        class_name = self.__name__
        return sum(1 for key in objects if key.startswith(f"{class_name}."))

