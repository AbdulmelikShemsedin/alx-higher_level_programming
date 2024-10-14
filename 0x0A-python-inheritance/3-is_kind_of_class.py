#!/usr/bin/python3
""" fucntion that checks instance"""


def is_kind_of_class(obj, a_class):
    """ returns true for correct instance"""
    if isinstance(obj, a_class):
        return True
    return False
