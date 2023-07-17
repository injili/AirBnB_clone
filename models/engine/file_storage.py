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
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects obj with a key
        key:
            <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes the __objects dictionary to the JSON file
        """
        file_name = FileStorage.__file_path
        with open(FileStorage.__file_path, mode="w") as f:
            serialized = {}
            for x,y in FileStorage.__objects.items():
                serialized[x] = y.to_dict()
            json.dump(serialized, f)

    def reload(self):
        """
        deseralizes the JSON file  to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
                return
