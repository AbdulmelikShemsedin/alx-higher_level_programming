#!/usr/bin/python3
""" the rectangle class module"""


class Rectangle:
    """ the rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantation of the class"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ A staticmethod returns the biggest rec"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ a class method"""
        return (cls(size, size))

    def __str__(self):
        str_t = ""
        if self.__width == 0 or self.__height == 0:
            return str_t
        for i in range(self.__height):
            for j in range(self.__width):
                str_t += str(self.print_symbol)
            if i == self.__height - 1:
                break
            str_t += "\n"
        return str_t

    def __repr__(self):
        str_t = "Rectangle(" + str(self.__width) + ", "
        str_t += str(self.__height) + ")"
        return str_t

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
