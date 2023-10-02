#!/usr/bin/python 3
# """"A module class """
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
    
#     '''A public instance of my_print'''
#     def my_print(self):
#         if self.__size == 0:
#             print ()
#         else:
#             for _ in range(self.__size):
#                 print("#" * self.__size)

#!/usr/bin/python3
"""
    Represents a square.
"""
class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square to be set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.

        If the size is equal to 0, print an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)