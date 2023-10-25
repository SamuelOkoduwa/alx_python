#!/usr/bin/python3

"""A Rectangle that inherits BaseGeometry"""
class BaseGeometry:
    """The class Base Geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
"""The inherited class Recyangle
"""
class Rectangle(BaseGeometry):
    """The instance"""
    def __init__(self, width, height):
        self.__width = 0  # Initialize width
        self.__height = 0  # Initialize height
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Set width
        self.__height = height  # Set height
