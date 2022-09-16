"""Sequence N"""


def main():
    """Main"""
    size = int(input())
    for col in range(size):
        for row in range(size):
            if col == row or row == (size - 1) or row == 0:
                print("*", end="")
            else:
                print("", end=" ")
        print()


main()
