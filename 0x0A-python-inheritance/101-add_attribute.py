#!/usr/bin/python3
"""This module contains a function that addss a new attribute to an object"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object
    Args:
        obj: object to which attribute is added
        name: name of attribute
        value: actual value of attribute
    Raises:
        TypeError: if object doesn't support adding attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
