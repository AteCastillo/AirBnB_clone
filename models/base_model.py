#!/usr/bin/python3
"""Base class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """new class"""
    def __init__(self, *args, **kwargs):
        """to initialize the class"""
        self.id = str(uuid4()) # to generate unique id
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    # to transform from string to datetime
                    self.__dict__[key] = datetime.strptime(value, time_format)
                    continue
                self.__dict__[key] = value

    def __str__(self):
        """to print"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today().isoformat()
        # isoformat to convert to string

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        # name returns only the name of the object
        for key, value in self.__dict__.items():
            if self.__dict__[key] is None:
                continue
            new_dict[key] = value
        return new_dict
