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
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes the __objects dictionary to the JSON file
        """
        file_name = FileStorage.__file_path
        serialized_data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(file_name, 'w', encoding="UTF-8") as f:
            json.dump(serialized_data, f)

    def reload(self):
        """
        deseralizes the JSON file  to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                    data = json.load(f)
                    for key,value in data.items():
                        FileStorage.__objects[key] = value
            except:
                pass
