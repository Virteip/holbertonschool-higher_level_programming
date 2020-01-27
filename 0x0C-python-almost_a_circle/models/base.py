#!/usr/bin/python3
"""
Base module
"""
import json
import os


class Base:
    """
    Class BAse
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class Base
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Return JSON representation of list_dictionaries
        """
        new_list = []
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string(new_list))
            else:
                for items in list_objs:
                    new_list.append(items.to_dictionary())
                new_list = cls.to_json_string(new_list)
                file.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Return list from JSON representation
        """
        if json_string is None or json_string is "":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return list from JSON representation
        """
        if cls.__name__ == "Rectangle":
            res = cls(8, 8)
        elif cls.__name__ == "Square":
            res = cls(24)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """
        Return list of instances
        """
        new_list = []
        name = cls.__name__ + ".json"
        if os.path.isfile(name):
            with open(name, 'r') as file:
                read_line = file.read()
                list_from_clsdict = cls.from_json_string(read_line)
                for line in list_from_clsdict:
                    new_list.append(cls.create(**line))
                return new_list
        else:
            return new_list
