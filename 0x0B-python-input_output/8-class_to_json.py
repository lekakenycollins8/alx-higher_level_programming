#!/usr/bin/python3
"""Module with function that returns the dictionary description
    with simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """Args: obj: instance of a class
    Returns:  the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
