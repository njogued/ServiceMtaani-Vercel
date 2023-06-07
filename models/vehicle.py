#!/usr/bin/python3
"""
Class for vehicles owned by client
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Vehicle(BaseModel, Base):
    """Vehicle attributes"""
    __tablename__ = "vehicles"
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    make = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    body_type = Column(String(30), nullable=False)
    year_of_manufacture = Column(Integer, nullable=False)
    
    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)