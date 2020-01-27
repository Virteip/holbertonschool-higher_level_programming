#!/usr/bin/python3
"""
Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getters: width
        """
        return self.__width

    @property
    def height(self):
        """
        Getters: height
        """
        return self.__height

    @property
    def x(self):
        """
        Getters: x
        """
        return self.__x

    @property
    def y(self):
        """
        Getters: y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setters: width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Setters: height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Setters: x
        """
        if type(value) == int and value >= 0:
            self.__x = value
        elif type(value) != int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """
        Setters: y
        """
        if type(value) == int and value >= 0:
            self.__y = value
        elif type(value) != int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        Area
        """
        return self.__height*self.__width

    def display(self):
        """
        Print Rectangle using #s to stdout
        """
        if self.__width and self.__height:
            print('\n' * self.__y, end='')
            for i in range(0, self.__height):
                for j in range(self.__width):
                    if j == 0:
                        print(" " * self.__x, end='')
                    print("#", end='')
                if j <= self.__width:
                    print('\n', end='')
        else:
            print()

    def __str__(self):
        """
        Print rectangle info for programming details
        """
        return "[Rectangle] " + "(" + str(self.id) + ") "\
            + str(self.__x) + "/"\
            + str(self.__y) + " - " + str(self.__width) + "/"\
            + str(self.__height)

    def update(self, *args, **kwargs):
        """
        Args Update
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Dict Rep of Rectangle Class
        """
        dict_attr = {}
        attributes = ['x', 'y', 'id', 'width', 'height']
        for key in attributes:
            dict_attr.update({key: getattr(self, key)})
        return dict_attr
