#!/usr/bin/python3
"""Module with class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a rectangle
    Attributes: public class attribute: number_of_instances, print_symbol
        width: The width of rectangle
        height: The height of rectangle
        __init__(self, width=0, height=0)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes class instance
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            display.append(str(self.print_symbol) * self.__width)
        return '\n'.join(display)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """Returns the biggest rectangle based on the area.
        Args:
            rect_1: An instance of Rectangle
            rect_2: An instance of Rectangle.
        Returns: 
            The rectangle with the larger area
        Raises: 
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
            """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
