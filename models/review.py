#!/usr/bin/python3
"""
module review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The review model implementation
    """
    place_id = ""
    user_id = ""
    text = ""
