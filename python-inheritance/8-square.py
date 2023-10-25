#!/usr/bin/python3

"""The class BaseGeometry"""
class BaseGeometry:
    """The area function that raises and exception"""
    def area(self):
        raise Exception("area() is not implemented")
    """The Integer validation""" 
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
"""The unherited class"""
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
