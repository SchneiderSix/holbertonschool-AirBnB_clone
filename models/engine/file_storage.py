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
        _d = {}
        for key in self.__objects:
            _d[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as sf:
            json.dump(my_d, sf)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                _o = json.load(rf)
                for key in _o:
                    self.__objects[key] = model[_o[key]["__class__"]](**_o[key])
        except:
            pass
