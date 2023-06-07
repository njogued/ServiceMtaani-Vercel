#!/usr/bin/python3

"""
Reviews Class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Review(BaseModel, Base):
    """Review attributes"""
    __tablename__ = "reviews"
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    vendor_id = Column(String(60), ForeignKey('vendors.id'))
    mechanic_id = Column(String(60), ForeignKey('mechanics.id'))
    description = Column(String(300))
    rating = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)
