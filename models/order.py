#!/usr/bin/python3
"""Class for orders"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

partorders = Table("parts_orders", Base.metadata,
                   Column("part_id", String(50), ForeignKey("parts.id", 
                          onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
                   Column("order_id", String(50), ForeignKey("orders.id",
                          ondelete="CASCADE", onupdate="CASCADE"), primary_key=True))


class Order(BaseModel, Base):
    """Order attributes"""
    __tablename__ = "orders"
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    status = Column(Boolean, default=True)
    parts = relationship("Part", secondary=partorders, backref="orders", cascade="all, delete")

    def __init__(self, **kwargs):
        """initialize the subclass using the superclass"""
        super().__init__(**kwargs)