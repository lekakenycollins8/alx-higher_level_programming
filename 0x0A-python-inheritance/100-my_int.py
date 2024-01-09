#!/usr/bin/python3
"""This module contains a subclass of int"""


class MyInt(int):
    """a subclass that inherits from int"""
    def __eq__(self, other):
        """overides the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """overides the != operator"""
        return super().__eq__(other)
