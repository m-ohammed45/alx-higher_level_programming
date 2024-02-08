#!/usr/bin/python3
"""
creat new class named rectangle
"""


class Rectangle:
    """class represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize our rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """get theier height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set their width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """get the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """get the perimeter of our rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """print rectangle with specific char"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width
             for _ in range(self.__height)]
        )

    def __repr__(self):
        """return statment about our rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """use it to delete the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """determine which rectangle is bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """creat a rectangle with width equal height"""
        return cls(size, size)
