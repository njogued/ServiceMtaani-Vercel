#!/usr/bin/python3
"""
Class Bids
"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column, ForeignKey, Boolean

class Bid(BaseModel, Base):
    """Bid attributes"""
    __tablename__ = 'bids'
    mechanic_id = Column(String(50), ForeignKey('mechanics.id'), nullable=False)
    job_id  = Column(String(50), ForeignKey('jobs.id'), nullable=False)
    bid_amount = Column(Integer, nullable=False, default=0)
    bid_status = Column(Integer, nullable=False, default=0)

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)
