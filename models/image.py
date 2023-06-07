#!/usr/bin/python3
"""
Module for the images table
"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Image(BaseModel, Base):
    """Initialize the images column"""
    __tablename__ = "images"
    part_id = Column(String(60), ForeignKey('parts.id'), nullable=False)
    image_path = Column(String(200), nullable=False)

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)
