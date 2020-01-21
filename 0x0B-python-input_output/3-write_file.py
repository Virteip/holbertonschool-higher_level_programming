#!/usr/bin/python3


def write_file(filename="", text=""):
    line_number = 0
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)
