#!/usr/bin/python3
"""This module contains a function that return the list of
    available attributes and methods of an object
    """


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Args:
        obj: object to look up
        Return: list of attributes and methos of object
    """
    return (dir(obj))
