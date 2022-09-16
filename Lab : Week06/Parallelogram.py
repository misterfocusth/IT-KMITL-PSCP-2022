"""Parallelogram"""


def main():
    """Main Function"""
    txt = input()
    space_multiplier = len(txt)
    for val_x in range(1, len(txt) + 1):
        print(" " * (space_multiplier - val_x), end="")
        print(txt[0:val_x])
    for val_y in range(1, len(txt) + 1):
        print(txt[val_y: len(txt)])


main()
