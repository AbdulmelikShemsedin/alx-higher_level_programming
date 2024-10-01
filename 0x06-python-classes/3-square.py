#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ rep... of a square class"""

    def __init__(self, size=0):
        """ instantation with size for our obect
        initialization
        """
        if size != int(size):
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size

    def area(self):
        """ method returns the current square area"""
        return (self.__size ** 2)
