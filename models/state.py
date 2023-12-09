#!/usr/bin/python3
"""Importing BaseModel."""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()

