"""Century"""

import math


def calculate_century(year):
    """Calculate century and return value"""
    if year < 1:
        return "ERROR"
    elif year >= 1 and year <= 100:
        return 1
    else:
        return int(math.ceil(year / 100))


def main():
    """Main Function"""
    numbers = int(input())
    for _ in range(numbers):
        input_year = input()
        year = int(input_year[5:])
        if "B.E." in input_year:
            year = year - 543
        print(calculate_century(year))


main()
