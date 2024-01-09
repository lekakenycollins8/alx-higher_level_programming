#!/usr/bin/python3
"""This module contains a function that deserializes an object"""


import json


def from_json_string(my_str):
    """Args:
            my_str: string to deserialize
        Returns: an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
