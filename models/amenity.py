#!/usr/bin/python3
"""Importing BaseModel."""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance with a unique id."""
        super().__init__()
        self.name = ""
