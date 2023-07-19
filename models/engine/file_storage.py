#!/usr/bin/python3
"""
module file_storage
"""
import json

from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects obj with a key
        key:
            <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes the __objects dictionary to the JSON file
        """
        file_name = self.__file_path
        with open(file_name, mode="w") as f:
            serialized = {}
            for x, y in self.__objects.items():
                serialized[x] = y.to_dict()
            json.dump(serialized, f)

    def reload(self):
        """
        deseralizes the JSON file  to __objects
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
                return
