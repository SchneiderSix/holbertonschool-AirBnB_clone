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
        with open(self.__file_path, 'w+') as sf:
            json.dump(self.__objects, sf,  indent=4)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                my_dict = json.loads(rf.read())
                for key, value in my_dict.items():
                    self.new(my_dict[value["__class__"]](**value))
        except:
            pass
