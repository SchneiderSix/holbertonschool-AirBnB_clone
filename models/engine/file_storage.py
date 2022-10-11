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
        ed = {}
        for key in self.__objects:
            ed[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as sf:
            json.dump(ed, sf)

    def reload(self):
        """Deserializes from json"""
        try:
            with open(self.__file_path) as rf:
                jl = json.loads(rf.read())
                for value in jl.values():
                    self.new(BaseModel(**value))
        except:
            pass
