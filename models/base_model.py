#!/usr/bin/python3
"""
Module Base
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class Base"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String expression of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates ins att with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary with keys/values of __dict__ of the instance"""
        el = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                el[key] = value.isoformat()
            else:
                el[key] = value
            el["__class__"] = self.__class__.__name__
        return el
