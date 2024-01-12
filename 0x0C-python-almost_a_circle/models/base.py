#!/usr/bin/python3
"""Module with a class named Base"""


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
