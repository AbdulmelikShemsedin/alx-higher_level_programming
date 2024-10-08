#!/usr/bin/python3
""" the rectanle class module"""


class Rectangle:
    """ the rectanle class"""
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
            print("width must be an integer")
            raise TypeError
        elif value < 0:
            print("width must be >= 0")
            raise ValueError
        self.__width = value

    @property
    def height(self):
        """ the getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter for the height"""
        if type(value) is not int:
            print("height must be an integer")
            raise TypeError
        elif value < 0:
            print("height must be >= 0")
            raise ValueError
        self.__height = value

    def area(self):
        """pub inst... method to cal.. the area"""
        return self.__width * self.__height

    def perimeter(self):
        """pub inst... method to cal.. the peri..."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
