#!/usr/bin/python 3

""""A module class """
class Square:
    """A private instance"""
    def __init__(self, size=0):
        self.__size = size
        
    """Property to retrieve instance of the class"""
    @property
    def size(self):
        return self.__size
    
    """property setter of value argument"""
    @property.setter
    def size(self, value):
        self.__value = value
        if type(value) != int:
            raise TypeError (" size must be an integer")
        if value < 0:
            raise ValueError ("size must be >= 0")
        
    """A Public instance method of area"""
    def area(self):
        """the square of the current area"""
        return self.__size * self.__size
    
    '''A public instance of my_print'''
    def my_print(self):
        if self.__size == 0:
            print ()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)