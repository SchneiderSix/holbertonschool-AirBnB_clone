#!/usr/bin/python3
"""
Call from file_storage
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
