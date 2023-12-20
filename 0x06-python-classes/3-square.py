#!/usr/bin/python3
"""Defines class square."""


class Square:
    """Square module."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side square.
        Raise:
            TypeError: if size not square
            ValueError: if size less then 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if 0 > size:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of squase.
        return:
            size squase.
        """
        return self.__size ** 2
