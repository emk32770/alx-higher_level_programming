#!/usr/bin/python3
"""
This script defines a Rectangle class that can calculate the area and perimeter of a rectangle
"""

class Rectangle:
    """Class that represents a rectangle"""
    
    def __init__(self, w=0, h=0):
        """Initializes the rectangle with the given width and height"""
        self.width = w
        self.height = h

    @property
    def width(self):
        """Finds the method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Places the method for the width attribute"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0")
        self.__width = value

    @property
    def height(self):
        """Finds the method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Places the method for the height attribute"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

