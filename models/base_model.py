#!/usr/bin/python3
"""
This is the module base_model
"""
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """
    This class defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Instance attributes
        Initialization of class BaseModel
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        return object representation in a string format
        """
        return ("[{:s}] ({:s}) {:s}".format(self.__class__.__name__,
                self.id, str(self.__dict__)))

    def save(self):
        """
        update the update_at attribute each time it is updated
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary of the instance
        created_at in string object ISO format
        updated_at in string object ISO format
        """

        di = self.__dict__.copy()
        di['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                value = self.__dict__[key].isoformat()
                di[key] = value

        return (di)
