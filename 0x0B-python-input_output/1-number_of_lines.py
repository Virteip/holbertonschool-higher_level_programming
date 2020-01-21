#!/usr/bin/python3


def number_of_lines(filename=""):
    line_number = 0
    with open(filename, 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
        return line_number
