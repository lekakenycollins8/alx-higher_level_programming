#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Attributes:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width, height):
        """initializes instance"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
