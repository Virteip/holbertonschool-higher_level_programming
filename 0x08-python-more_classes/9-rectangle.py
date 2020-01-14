#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    """
    Init method to set width and height variables.
    """
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    """
    Getter Heigth
    """
    @property
    def height(self):
        return self.__height

    """
    Setter Height
    """
    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        elif type(value) != int:
            raise NameError("height must be an integer")
        elif value < 0:
            raise NameError("height must be >= 0")

    """
    Getter Width
    """
    @property
    def width(self):
        return self.__width

    """
    Setter Width
    """
    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        elif type(value) != int:
            raise NameError("width must be an integer")
        elif value < 0:
            raise NameError("width must be >= 0")

    """
    Area
    """
    def area(self):
        return self.__height*self.__width

    """
    Perimeter
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * (self.__height + self.__width)
        return self.__perimeter

    """
    Print rectangle as string and user readability
    """
    def __str__(self):
        square = []
        if self.__width and self.__height:
            for i in range(0, self.__height):
                for j in range(self.__width):
                    square.append(str(self.print_symbol))
                if j <= self.__width:
                    square.append('\n')
            return "".join(square[:-1])
        else:
            square = ''
            return square

    """
    Print rectangle info for programming details
    """
    def __repr__(self):
        return "Rectangle" + "(" + str(self.__width)\
            + ", " + str(self.__height) + ")"
    """
    Print message when deleting an instance
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """
    Return biggest rectangle
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) and isinstance(rect_2, Rectangle):
            if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
                return rect_1
            else:
                return rect_2
        elif not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

    """
    Return square
    """
    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
