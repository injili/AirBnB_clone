#!/usr/bin/python3
"""
module file_storage
"""
import json
import os


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def __init__(self):
        """
        instance constructor with the
        attributes:
            __file_path: the string path to the JSON file
            __objects: the dictionary thatstores all the objects
        """
        self.__file_path = "file.json"
        self.__objects = {}


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
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes the __objects dictionary to the JSON file
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deseralizes the JSON file  to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        else:
            pass
