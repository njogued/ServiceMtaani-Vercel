#!/usr/bin/python3
"""This module contains the Base Class for Clients, Mechanics
and Vendors Classses
"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()
time = "%m/%d/%Y, %H:%M:%S"

class BaseModel():
    """Class to base all other classes on"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        if kwargs:
            if id not in kwargs.keys():
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
                # Update to handle incase created_at or updated_at is missing
            for key, value in kwargs.items():
                setattr(self, key, value)
                # storage.new(self)
    
    def __str__(self):
        """Return a string representation of the object"""
        attributes_dict = self.__dict__.copy()
        attributes_dict['created_at'] = attributes_dict['created_at'].strftime(time)
        attributes_dict['updated_at'] = attributes_dict['updated_at'].strftime(time)
        return f"Class: {self.__class__.__name__}, ID: {self.id}, DETAILS: {attributes_dict}"
    
    def to_str(self):
        attributes_dict = self.__dict__.copy()
        attributes_dict['created_at'] = attributes_dict['created_at'].strftime(time)
        attributes_dict['updated_at'] = attributes_dict['updated_at'].strftime(time)
        return f"Class: {self.__class__.__name__}, ID: {self.id}, DETAILS: {attributes_dict}"
    
    def to_dict(self):
        """returns a dict containing all k,v of instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    
    def save(self):
        """Save the object to the database"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def delete(self):
        """Delete the object from the database"""
        models.storage.delete(self)
        models.storage.save()

    def update(self, attr, value):
        """Update the object attributes"""
        if attr in self.__dict__.keys() and attr != "id":
            setattr(self, attr, value)
        models.storage.save()
