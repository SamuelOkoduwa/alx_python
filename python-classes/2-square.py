#!/usr/bin/python3

"""A Class Square"""
class Square:
    """Instance of  class"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ('size must be >= 0')
    
    """A public instance method"""
    def area(self):
        '''Returns the current square'''
        return self.__size ** 2
    