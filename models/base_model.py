#!/usr/bin/python3
"""Import necessary modules."""

from uuid import uuid4
from datetime import datetime
import models

"""BaseModel class."""


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        if args is not None and len(args) > 0:
            pass
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at
            with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        instance_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            instance_dict[key] = value
        return instance_dict

