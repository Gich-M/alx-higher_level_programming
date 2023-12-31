#!/usr/bin/python3

class Square:
    """Class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if value < 0:
                raise TypeError


    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
