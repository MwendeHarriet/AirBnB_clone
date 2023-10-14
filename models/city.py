#!/usr/bin/python3
"""
    This module defines the class City.
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class city inherits from BaseModel.
    """
    state_id = ""
    name = ""
