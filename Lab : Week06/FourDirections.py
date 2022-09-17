"""FourDirections"""


def main():
    """Main Function"""
    directions = input()
    for i in range(len(directions)):
        print_first_line()
    print()
    for i in range(len(directions)):
        print_second_line(directions, i)
    print()
    for i in range(len(directions)):
        print_third_line(directions, i)
    print()
    for i in range(len(directions)):
        print_fourth_line(directions, i)
    print()
    for i in range(len(directions)):
        print_first_line()
    print()


def print_first_line():
    """Print first line"""
    print("  *  ", end=" ")


def print_second_line(directions, index):
    """Print second line"""
    if directions[index] == "U":
        print(" *** ", end=" ")
    elif directions[index] == "D":
        print("  *  ", end=" ")
    elif directions[index] == "L":
        print(" *   ", end=" ")
    elif directions[index] == "R":
        print("   * ", end=" ")


def print_third_line(directions, index):
    """Print third line"""
    if directions[index] in "UD":
        print("* * *", end=" ")
    elif directions[index] in "LR":
        print("*****", end=" ")


def print_fourth_line(directions, index):
    """Print fourth line"""
    if directions[index] == "U":
        print("  *  ", end=" ")
    elif directions[index] == "D":
        print(" *** ", end=" ")
    elif directions[index] == "L":
        print(" *   ", end=" ")
    elif directions[index] == "R":
        print("   * ", end=" ")


main()
