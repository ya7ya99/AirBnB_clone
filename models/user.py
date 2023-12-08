#!/usr/bin/python3
"""Import necessary modules."""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel

"""User class that inherits from BaseModel."""


class User(BaseModel):
    """User class that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        if not kwargs:
            super().__init__()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

