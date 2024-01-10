#!/usr/bin/python3
"""Module with functio that inserts a line of text to a file,
    after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    Args:
        filename: name of file to be modified
        search_string: string to be searched for
        new_string: string to be added after search string
    Returns: modified file
    """
    with open(filename, "r") as f1:
        content = f1.readlines()
    with open(filename, "w") as f2:
        for line in content:
            f2.write(line)
            if search_string in line:
                f2.write(new_string)
