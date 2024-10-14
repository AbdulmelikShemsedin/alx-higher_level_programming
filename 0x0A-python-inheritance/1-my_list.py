#!/usr/bin/python3
""" class that inherits list"""


class MyList(list):
    """ class that inheits"""
    def print_sorted(self):
        """ func that sots and prints list"""
        print(sorted(self))
