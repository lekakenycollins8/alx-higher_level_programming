#!/usr/bin/python3
"""Module with class square that inherits from class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from class rectangle
    Attributes:
        size: size of the square
        x- position on x axis
        y- position on y-axis
        id - class id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """instanstiation of attributes"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.__size = size
    
    def __str__(self):
        """string representation of square"""
        s = self.__class__.__name__
        x = self.x
        y = self.y
        w = self.width
        return "[{}] ({}) {}/{} - {}".format(s, self.id, x, y, w)

    @property
    def size(self):
        """width getter"""
        return self.__width

    @Rectangle.width.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

