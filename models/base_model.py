#!/usr/bin/python3
"""
Module Base
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class Base"""
    def __init__(self):
        """Constructor"""
        self.id = str(uuid4())
        self.created_at = datatime.now()
        self.updated_at = datatime.now()

    def __str__(self):
        """String expression of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates ins att with current datatime"""
        self.updated_at = datatime.now()

    def to_dict(self):
        """Dictionary with keys/values of __dict__ of the instance"""
        el = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                el[key] = value.isoformat()
            else:
                el[key] = value
        return el
