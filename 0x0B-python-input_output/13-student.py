#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            output = self.__dict__
        elif attrs:
            output = {}
            for position in range(0, len(attrs)):
                if attrs[position] in self.__dict__:
                    output[attrs[position]] = self.__dict__[attrs[position]]
        return (output)

    def reload_from_json(self, json):
        for position in json.keys():
            self.__dict__[position] = json[position]
