#!/usr/bin/python3
"""
Module File Storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def classx(self):
        """Dict with all calsses"""
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel, "Amenity": Amenity,
                "City": City, "Place": Place,
                "Review": Review, "State": State, "User": User}
        return classes

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
        from models.base_model import BaseModel
        try:
            with open(self.__file_path) as rf:
                for key, value in json.load(rf).items():
                    self.__objects(key) = BaseModel(**value)
        except:
            pass
