#!/usr/bin/python3
"""
Class for mechanics
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class Mechanic(BaseModel, Base, UserMixin):
    __tablename__ = "mechanics"
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    phone_number = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)
    business_name = Column(String(60))
    jobs_completed = Column(Integer, nullable=False, default=0)
    rating = Column(Integer, nullable=False, default=0)
    specialization = Column(String(60))
    bids = relationship("Bid", backref="mechanic", cascade="all, delete, delete-orphan")
    reviews = relationship("Review", backref="mechanic", cascade="all, delete, delete-orphan")

    # def is_authenticated():
    #     return True
    # def is_active():
    #     return True
    # def is_anonymous():
    #     return True
    # def get_id():
    #     return

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)
