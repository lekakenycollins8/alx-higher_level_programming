#!/usr/bin/python3
"""Module contains function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """creates an object from JSON file
    Args:
        filename: JSON filename
    """
    with open(filename, encoding="utf-8") as f1:
        return json.loads(f1.read())
