#!/usr/bin/python3
"""
Module Base
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class Base"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """String expression of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates ins att with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary with keys/values of __dict__ of the instance"""
        ndic = dict(self.__dict__)
        ndic["__class__"] = self.__class__.__name__
        ndic["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        ndic["updated_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return ndic
