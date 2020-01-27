#!/usr/bin/python3
"""
Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    Initializer method
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """
    Getters: width
    """
    @property
    def width(self):
        return self.__width
    
    """
    Getters: height
    """
    @property
    def height(self):
        return self.__height
    
    """
    Getters: x
    """
    @property
    def x(self):
        return self.__x
    
    """
    Getters: y
    """
    @property
    def y(self):
        return self.__y

    """
    Setters: width
    """
    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        elif type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
    
    """
    Setters: height
    """
    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        elif type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
    
    """
    Setters: x
    """
    @x.setter
    def x(self, value):
        if type(value) == int and value >= 0:
            self.__x = value
        elif type(value) != int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
    
    """
    Setters: y
    """
    @y.setter
    def y(self, value):
        if type(value) == int and value >= 0:
            self.__y = value
        elif type(value) != int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")

    """
    Area
    """
    def area(self):
        return self.__height*self.__width

    """
    Print Rectangle using #s to stdout
    """
    def display(self):
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

    """
    Print rectangle info for programming details
    """
    def __str__(self):
        return "[Rectangle] " + "(" + str(self.id) + ") "\
            + str(self.__x) + "/"\
            + str(self.__y) + " - " + str(self.__width) + "/"\
            + str(self.__height)

    """
    Args Update
    """
    def update(self, *args, **kwargs):
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

    """
    Dict Rep of Rectangle Class
    """
    def to_dictionary(self):
        dict_attr = {}
        attributes = ['x', 'y', 'id', 'width', 'height']
        for key in attributes:
            dict_attr.update({key: getattr(self, key)})
        return dict_attr
