#!/usr/bin/python3
"""Module contains function that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to write to file
        filename: name of text file
    """
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
