#!/usr/bin/python3

class Square:
    """Class defines a square and returns the current square area"""

    def __init__(self, size):
        self.__size = size

        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError) as error:
            print(error)


    def area(self):
        return self.__size ** 2
