"""Sequence VII // https://ejudge.it.kmitl.ac.th/problem/8179"""


def print_top(height):
    """Print top"""
    for val_x in range(1, height + 1):
        for current_num in range(1, val_x + 1):
            print(current_num, end=" ")
        if val_x != height + 1:
            print()


def print_bottom(height):
    """"Print bottom"""
    stop = height
    for val_x in range(1, height + 1):
        for current_num in range(1, stop):
            print(current_num, end=" ")
        stop -= 1
        if val_x != height + 1:
            print()


def main():
    """Main Function"""
    number = int(input())
    print_top(number)
    print_bottom(number)


main()
               