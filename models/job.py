#!/usr/bin/python3
"""
Jobs class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Job(BaseModel, Base):
    """Job attributes"""
    __tablename__ = "jobs"
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    job_title = Column(String(200), nullable=False)
    job_description = Column(String(500))
    job_status = Column(Integer, default=1)
    bids = relationship("Bid", backref="job", cascade="all, delete, delete-orphan")

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)
