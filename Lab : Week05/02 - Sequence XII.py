"""Sequence XII"""


def main():
    """Main Function"""
    number = int(input())
    for i in range(-number + 1, number, 1):
        for j in range(-number + 1, number, 1):
            print("%02d" % (number - abs(abs(i) - abs(j))), end=" ")
        print()


main()
