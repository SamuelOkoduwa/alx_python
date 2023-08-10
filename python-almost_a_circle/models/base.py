#1/usr/bin/python3
"""The Base Class"""
class Base:
    """private Class Atttribute"""
    __nb__objects = 0
    """A class constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects