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
        x_x = self.x
        y_y = self.y
        w = self.__size
        return "[{}] ({}) {}/{} - {}".format(s, self.id, x_x, y_y, w)

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

    def update(self, *args, **kwargs):
        """assigns attributes to object"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
                self.y = args[3]
        if not args:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """dictionary representation of square"""
        sq_dict = {}
        sq_dict['id'] = self.id
        sq_dict['size'] = self.__size
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y
        return sq_dict
