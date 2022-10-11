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
            my_d = {}
            for key, value in self.__objects.items():
                my_d[key] = value.to_dict()
            json.dump(my_d, sf)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                my_o = json.load(rf)
                for key, value in my_o.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass

