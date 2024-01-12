#!/usr/bin/python3
"""Module with class that inherits from base class"""


from models.base import Base


class Rectangle(Base):
    """inherits from base class
    Attributes:
        private instance attributes: width, height, x, y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instance attributes
        Args:
            width-of rectangle
            height-of rectangle
            x- coordinate position of Rectangle
            y- coordinate position of rectangle
            id- class id
        """
        super().__init__(id=id)
        if not isinstance(width, int):
            raise TypeError("width must be an intger")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """validating all setter methods"""

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
        
    @property
    def height(self, value):
        """height getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >=0")

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the display of rectangle with #"""
        for i in range(self.__height):
            print("#" * self.__width)
