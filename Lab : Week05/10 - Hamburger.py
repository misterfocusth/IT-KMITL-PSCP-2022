"""Hamburger"""


def main():
    """Main Function"""
    left = int(input())
    right = int(input())
    middle = (left+right) * 2
    print("%s%s%s" % (("|" * left), ("*" * middle), ("|" * right)))


main()
