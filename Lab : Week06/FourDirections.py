"""FourDirections"""


def main():
    """Main Function"""
    directions = input()
    for i in range(len(directions)):
        line1()
    print()
    for i in range(len(directions)):
        line2(directions, i)
    print()
    for i in range(len(directions)):
        line3(directions, i)
    print()
    for i in range(len(directions)):
        line4(directions, i)
    print()
    for i in range(len(directions)):
        line1()
    print()


def line1():
    """Line1"""
    print("  *  ", end=" ")


def line2(password, index):
    """Line2"""
    if password[index] == "U":
        print(" *** ", end=" ")
    elif password[index] == "D":
        print("  *  ", end=" ")
    elif password[index] == "L":
        print(" *   ", end=" ")
    elif password[index] == "R":
        print("   * ", end=" ")


def line3(password, index):
    """Line3"""
    if password[index] in "UD":
        print("* * *", end=" ")
    elif password[index] in "LR":
        print("*****", end=" ")


def line4(password, index):
    """Line4"""
    if password[index] == "U":
        print("  *  ", end=" ")
    elif password[index] == "D":
        print(" *** ", end=" ")
    elif password[index] == "L":
        print(" *   ", end=" ")
    elif password[index] == "R":
        print("   * ", end=" ")


main()
