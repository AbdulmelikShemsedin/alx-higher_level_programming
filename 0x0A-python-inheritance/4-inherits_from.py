#!/usr/bin/python3
""" fucntion that checks instance"""


def inherits_from(obj, a_class):
    """ returns true for correct instance"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
