#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, w=0, h=0):
        """Initializes the rectangle"""
        self.width = w
        self.height = h

    @property
    def width(self):
        """finds the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """places the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """finds the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """places the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
