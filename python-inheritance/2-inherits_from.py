#!usr/bin/python3
"""
 a function that returns True if the object is an instance of a class that inherited
"""
def inherits_from(obj, a_class):
    """
    the classes of object's type that hierarchy
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

