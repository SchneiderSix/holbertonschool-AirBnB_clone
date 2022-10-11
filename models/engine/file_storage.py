#!/usr/bin/python3
"""
Module File Storage
"""
import json


class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dic of obj"""
        return self.__objects

    def new(self, obj):
        """Set new object"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

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

    def save(self):
        """Serializes to json"""
        ob = {}
        for key in self.__objects:
            ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as sf:
            json.dump(ob, sf)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                dictjson = json.load(rf)
        except:
            pass
