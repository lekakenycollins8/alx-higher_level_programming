#!/usr/bin/python3
"""This module contains a function that returns True if
    the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """"returns True if the object is exactly an
    instance of the specified class
    Args:
        obj: instance of class
        a_class: specified class
    Returns: True if the object is exactly an instance
                of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
