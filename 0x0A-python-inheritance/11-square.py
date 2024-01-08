#!/usr/bin/python3
"""This module contains a subclass of class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    Attributes: size: size of square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """return square description"""
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__size, self.__size)
