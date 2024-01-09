#!/usr/bin/python3
"""Module contains a function that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """appends string at end of text file
    Args:
        filename: name of the file
        text: string to append
    Returns:  the number of characters added
    """
    with open(filename, "a") as f1:
        f1.write(text)
    return len(text)
