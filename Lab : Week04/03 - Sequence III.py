"""Sequence III // https://ejudge.it.kmitl.ac.th/problem/8175"""


def main():
    """Main Function"""
    number = int(input())
    for val_x in range(1, number + 1):
        for val_y in range(1, number + 1):
            print(val_y + val_x, end=" ")
        if val_x != (number + 1):
            print()
            
    for x in range(1, number + 1, 1):
        for y in range(1, number + 1, 1):
            print(x + y, end=" ")
        if x != (number + 1):
            print()


main()


