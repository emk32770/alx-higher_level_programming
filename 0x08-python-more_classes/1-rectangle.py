#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class representation of a rectangle"""
    def __init__(self, width=0, height=0):
     """initializes a Rectangle instance with width and height"""
     self.height = height
     self.width = width

    @property
    def width(self):
        """returns the width value of the rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """places the width value of the rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """peturns the height value of the rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """places the height value of the rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
