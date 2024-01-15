#!/usr/bin/python3
"""Module with a class named Base"""


import json


class Base:
    """This is the Base class
    Attributes:
        private class attribute: __nb_objects
    Constructor:
        def __init__(self, id=None)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """initializes class instance
        Args:
            id: class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None or "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f1:
            j_str = cls.to_json_string([i.to_dictionary() for i in list_objs])
            f1.write(j_str)
