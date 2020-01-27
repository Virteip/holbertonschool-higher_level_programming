#!/usr/bin/python3
import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """
    Return JSON representation of list_dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        file = json.dumps(list_dictionaries)
        return file

    """
    Return JSON representation of list_dictionaries
    """
    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string(new_list))
            else:
                for items in list_objs:
                    new_list.append(items.to_dictionary())
                new_list = cls.to_json_string(new_list)
                file.write(new_list)

    """
    Return list from JSON representation
    """
    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    """
    Return list from JSON representation
    """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            res = cls(8, 8)
        elif cls.__name__ == "Square":
            res = cls(24)
        res.update(**dictionary)
        return res
