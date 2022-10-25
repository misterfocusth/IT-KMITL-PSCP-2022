"""Hamburger"""


def main():
    """Main Function"""
    left_bread = int(input())
    right_bread = int(input())
    meat = "*" * ((left_bread + right_bread) * 2)
    left = "|" * left_bread
    right = "|" * right_bread
    print(left, meat, right, sep="")


main()
