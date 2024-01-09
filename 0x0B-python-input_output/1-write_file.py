#!/usr/bin/python3
"""This module contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename: name of file to write from
        text: string to write to file
    Returns:
        the number of characters written
    """
    with open(filename, "w") as f1:
        f1.write(text)
    return len(text)
