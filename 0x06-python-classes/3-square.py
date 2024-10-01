#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if size != int(size):
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError
    def area(self):
        return self.__size ** 2
