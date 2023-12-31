#!/usr/bin/python3

class Square:
    """Class defining a square"""
    def __init__(self, size=0):
        self.__size = size
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError) as error:
            print(error)
