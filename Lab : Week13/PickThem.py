"""PickThem"""

import json


def main():
    """Main Function"""
    numbers = json.loads(input())
    even_nums = []
    for val_x in numbers:
        number = int(val_x)
        if number % 2 == 0:
            even_nums.append(int(val_x))
    if len(even_nums) > 0:
        print(*even_nums, sep="\n")
    else:
        print("Nope")


main()
