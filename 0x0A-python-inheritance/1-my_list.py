#!/usr/bin/python3
"""This module contains a class MyList that inherits from list"""


class MyList(list):
    """ a class that inherits from list
    Args:
        list: base class
    Attributes: print_sorted- Prints sorted list
    """
    
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
