#!/usr/bin/python3
"""Base class"""



class FileStorage:
    """new class"""
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode="w") as f:
            f.write(json.dump(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r") as f:


