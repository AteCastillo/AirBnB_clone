#!/usr/bin/python3
"""Base Class"""


from uuid import uuid4
from datetime import datetime
import json
import models


class BaseModel():
    """Base Class description"""

    def __init__(self, *args, **kwargs):
        """Initialization function"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"  # format received
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    # to transform from string to datetime
                    current = datetime.strptime(value, time_format)
            # takes an attribute of a class and assign a value "current"
                    setattr(self, key, current)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())  # to generate unique id
            self.created_at = datetime.today()  # time created
            self.updated_at = datetime.today()  # time updated
            models.storage.new(self)

    def __str__(self):
        """Method that returns ..."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at"""
        current = datetime.today()
        self.updated_at = current
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        # name returns only the name of the object
        new_dict = self.__dict__.copy()
        # isoformat to convert to string
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
