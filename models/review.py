#!/usr/bin/python3
"""
    This module defines the class Review.
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
