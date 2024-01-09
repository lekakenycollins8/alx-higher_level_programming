#!/usr/bin/python3
"""This module contains a function that reads a text fil"""


def read_file(filename=""):
    """reads a text file and prints to stdout
    Args:
        filename: name of file to be read
    """
    with open(filename, "r") as file_1:
        print(file_1.read(), end="")
