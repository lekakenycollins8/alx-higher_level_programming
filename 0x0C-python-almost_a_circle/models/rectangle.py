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
        
