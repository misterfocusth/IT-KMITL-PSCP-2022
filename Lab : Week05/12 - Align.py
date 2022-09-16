"""Align"""

import math


def calculate_padding(text, size):
    """Calculate Padding before print"""
    return size - len(text)


def main():
    """Align"""
    size = int(input())
    position = input().lower()
    text = input()
    if position == "left":
        print(text + " " * calculate_padding(text, size))
    elif position == "right":
        print(" " * calculate_padding(text, size) + text)
    elif position == "center":
        padding_left = math.ceil(calculate_padding(text, size) / 2)
        padding_right = math.floor(calculate_padding(text, size) / 2)
        print(" " * padding_left + text + " " * padding_right)


main()
