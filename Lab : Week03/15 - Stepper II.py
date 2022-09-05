"""Stepper II // https://ejudge.it.kmitl.ac.th/problem/8167"""


def main():
    """Main Function"""
    start, stop = int(input()), int(input())
    if start > stop:
        for current in range(start, (stop - 1), -1):
            print(current)
    else:
        for current in range(start, stop + 1):
            print(current)


main()
