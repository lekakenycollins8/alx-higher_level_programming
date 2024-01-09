#!/usr/bin/python3
"""This module contains a function with Jsoon representation of an object"""


import json


def to_json_string(my_obj):
    """Args:
        my_obj: object to be serialized
        Returns: the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
