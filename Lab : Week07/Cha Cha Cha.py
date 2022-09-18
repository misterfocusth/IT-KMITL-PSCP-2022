"""Cha Cha Cha"""

import math


def main():
    """Main Function"""
    work_days = int(input())
    total_hours = 0
    for _ in range(work_days):
        total_hours += int(math.ceil(float(input())))
    print(int(8720 * total_hours))


main()
