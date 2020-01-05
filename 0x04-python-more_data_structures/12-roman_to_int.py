#!/usr/bin/python3
def roman_to_int(roman_string):
    r_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    outcome = 0
    ret = 0

    if not isinstance(roman_string, str):
        return 0

    for i in reversed(roman_string):
        ret = r_nums[i]
        outcome += ret if outcome < ret * 5 else -ret

    return outcome
