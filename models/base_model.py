#!/usr/bin/python3
"""
This is the module base_model
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    This class defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        instance attributes
        """
        self.name = kwargs.get('name', None)
        self.my_number = kwargs.get('my_number',None)
        self.id = kwargs.get( 'id', str(uuid4()))

        created_at = kwargs.get('created_at')
        if created_at:
            self.created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()

        updated_at = kwargs.get('updated_at')
        if updated_at:
            self.updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        return a dictionary of the instance
        created_at in string object ISO format
        updated_at in string object ISO format
        """
        di = self.__dict__.copy()
        di['created_at'] = self.created_at.isoformat()
        di['updated_at'] = self.updated_at.isoformat()
        di['__class__'] = self.__class__.__name__

        return (di)
