#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Starts the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """finds the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """places the private instance attribute width"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        rectangle = ""
        if self.__width != 0 and self.__height != 0:
            rectangle += "\n".join("#" * self.__width
                                   for xtr in range(self.__height))
        return rectangle

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    def __del__(self):
        """prints a message when instance is deleted"""
        print("Bye rectangle...")
