#!/usr/bin/python3
""" Define a square class"""
class Square:
    """ rep.. of a square class"""
    def __init__(self, size=0):
        """ instantation with size for our obect
        initialization
        """
        if size != int(size):
            raise TypeError("size must be an integer", end="")
        if size < 0:
            raise ValueError("size must be >= 0", end="")
        self.__size = size
