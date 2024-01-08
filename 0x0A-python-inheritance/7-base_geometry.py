#!/usr/bin/python3
"""This module contains class BaseGeometry"""


class BaseGeometry:
    """Base class
    Attributes:
        public instance method
    """
    def area(self):
        """public instance method
        Raise: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name: name of value
            value: value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
