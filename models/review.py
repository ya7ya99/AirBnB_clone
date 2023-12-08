#!/usr/bin/python3
"""Importing BaseModel."""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()

