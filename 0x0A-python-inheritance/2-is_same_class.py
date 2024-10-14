#!/usr/bin/python3
""" fucntion that checks instance"""


def is_same_class(obj, a_class):
    """ returns true for correct instance"""
    if type(obj) is a_class:
        return True
    return False
