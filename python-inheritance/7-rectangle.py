#!/usr/bin/python3

"""A class Base Geometry
"""
class BaseGeometry:
    """area self
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""The Rectangle Inheried from Base Geometry"""
class Rectangle(BaseGeometry):
    """The instance of the class"""
    def __init__(self, width, height):
        self.__width = 0  # Initialize width
        self.__height = 0  # Initialize height
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Set width
        self.__height = height  # Set height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
