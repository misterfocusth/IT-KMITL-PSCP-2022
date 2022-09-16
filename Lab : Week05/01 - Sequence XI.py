"""Sequence XI"""


def main():
    """Main Function"""
    number = int(input())
    for i in range(-number + 1, number, 1):
        for j in range(-number + 1, number, 1):
            if abs(i) > abs(j) - 1:
                print("%02d" % (number - abs(i)), end=" ")
            else:
                print("%02d" % (number - abs(j)), end=" ")
        print()


main()
