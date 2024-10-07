#!/usr/bin/python3
""" the rectangle class module"""


class Rectangle:
    """ the rectangle class"""
    def __init__(self, width=0, height=0):
        """ instantation of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ the getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """pub inst... method to cal.. the area"""
        return self.__width * self.__height

    def perimeter(self):
        """pub inst... method to cal.. the peri..."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str_t = ""
        if self.__width == 0 or self.__height == 0:
            return str_t
        for i in range(self.__height):
            for j in range(self.__width):
                str_t += "#"
            if i == self.__height - 1:
                break
            str_t += "\n"
        return str_t

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
