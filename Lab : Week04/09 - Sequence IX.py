"""Sequence VIII // https://ejudge.it.kmitl.ac.th/problem/8180"""


def main():
    """Main Function"""
    number = int(input())
    for val_x in range(1, number + 1):
        for _ in range(number - val_x):
            print("  ", end=" ")
        for current_num in range(1, val_x + 1):
            print("%02d" % current_num, end=" ")
        for current_num in range(val_x-1, 0, -1):
            print("%02d" % current_num, end=" ")
        print()


main()
