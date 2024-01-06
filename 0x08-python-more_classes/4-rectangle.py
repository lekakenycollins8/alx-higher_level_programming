#!/usr/bin/python3
"""Module with class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a rectangle
    Attributes:
        width: The width of rectangle
        height: The height of rectangle
        __init__(self, width=0, height=0)
    """
    def __init__(self, width=0, height=0):
        """initializes class instance
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves attribute
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method
        Args:
            value: new width value
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter method
        Returns:
            height: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method
        Args:
            value: width value
        Raises:
            TypeError:  if height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """returns area ofthe rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        display = []
        for i in range(self.__height):
            display.append("#" * self.__width)
        return '\n'.join(display)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
