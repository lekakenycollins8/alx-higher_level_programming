#!/usr/bin/python3
"""This module contains a function that returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """checks if object is a subclass
    Args:
        obj: object to check
        a_class: specified class
    Return: True if the object is an instance of a class that inherited
        from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
