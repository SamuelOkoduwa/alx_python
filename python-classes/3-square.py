#!/usr/bin/python3

# """A module with an object Square"""
# class Square:
#     """A private instance"""
#     def __init__(self, size=0):
#         self.__size = size
        
#     """Property to retrieve instance of the class"""
#     @property
#     def size(self):
#         return self.__size
    
#     """property setter of value argument"""
#     @property.setter
#     def size(self, value):
#         self.__value = value
#         if type(value) != int:
#             raise TypeError (" size must be an integer")
#         if value < 0:
#             raise ValueError ("size must be >= 0")
#     """A Public instance method of area"""
#     def area(self):
#         """the square of the current area"""
#         return self.__size * self.__size
    
    
#!/usr/bin/python3
"""A module containing a square"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value (int): new value of size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square
        Returns:
            area
        """

        return self.__size * self.__size