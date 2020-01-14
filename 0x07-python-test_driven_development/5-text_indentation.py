#!/usr/bin/python3


def text_indentation(text):
    if type(text) == str:
        for i in range(len(text)):
            if text[i - 1] in ".?:":
                continue
            print(text[i], end="")
            if text[i] in ".?:":
                print("\n")
    else:
        raise TypeError("text must be a string")
