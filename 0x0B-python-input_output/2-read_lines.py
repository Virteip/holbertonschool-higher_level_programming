#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    line_number = 0
    with open(filename, 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            if nb_lines == 0:
                print(a_line, end='')
            elif line_number < nb_lines:
                print(a_line, end='')
                line_number += 1
