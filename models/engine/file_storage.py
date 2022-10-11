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

    def save(self):
        """Serializes to json"""
        with open(self.__file_path, 'w') as sf:
            sv = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(sv, sf)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                self.__objects.update(json.load(rf))
        except:
            pass
