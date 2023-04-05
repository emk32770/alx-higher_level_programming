#!/usr/bin/python3
"""
This program defines a Rectangle class that represents a rectangle.
"""

class Rectangle:
    """This class represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with the given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Finds the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Places the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0")
        self.__width = value

    @property
    def height(self):
        """Finds the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Places the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
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
