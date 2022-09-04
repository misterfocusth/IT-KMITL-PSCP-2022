"""Sequence IV // https://ejudge.it.kmitl.ac.th/problem/8176"""


def main():
    """Main Function"""
    number = int(input())
    current_start, current_stop = 1, number
    for val_x in range(1, number + 1):
        for val_y in range(current_start, current_stop + 1):
            print(val_y, end=" ")
        current_start += number
        current_stop += number
        if val_x != (number + 1):
            print()


main()
