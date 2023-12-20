#!/usr/bin/python3
"""Defines class square."""


class Square:
    """Square module."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side square.
        """
        self.size = size

    @property
    def size(self):
        """property for length of sidesquase.
         Raise:
            TypeError: if size not square
            ValueError: if size less then 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if 0 > value:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of squase.
        return:
            size squase.
        """
        return self.__size ** 2
