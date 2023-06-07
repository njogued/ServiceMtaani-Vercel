#!/usr/bin/python3
"""
Class for vendors
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class Vendor(BaseModel, Base, UserMixin):
    __tablename__ = "vendors"
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    # phone_number = Column(Integer, nullable=False)
    phone_number = Column(String(30), nullable=False)
    business_name = Column(String(100), nullable=False)
    orders_completed = Column(Integer, default=0, nullable=False)
    rating = Column(Integer, default=0, nullable=False)
    parts = relationship("Part", backref="vendor", cascade="all, delete, delete-orphan")
    reviews  = relationship("Review", backref="vendor", cascade="all, delete, delete-orphan")

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)