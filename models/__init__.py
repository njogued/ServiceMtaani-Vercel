#!/usr/bin/python3
"""
Initialize the storage
"""
from models.engine.dbstorage import DBStorage
storage = DBStorage()
storage.reload()
