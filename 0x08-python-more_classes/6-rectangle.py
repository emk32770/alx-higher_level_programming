#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """Represents the rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
       """Initializes the rectangle"""
       self.width = width
       self.height = height
       Rectangle.number_of_instances += 1

    @property
    def height(self):
        """finds the private instance attribute height"""
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        """places the private instance attribute height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = height

    @property
    def width(self):
        """finds the private instance attribute width"""
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        """places the private instance attribute width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = width

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        rectangle = ""
        for xtr in range(self.height):
            for __ in range(self.width):
                rectangle += "#"
            if xtr < self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
