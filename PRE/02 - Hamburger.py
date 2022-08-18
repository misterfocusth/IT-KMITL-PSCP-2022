"""[Pre] Hamburger / https://ejudge.it.kmitl.ac.th/problem/8098"""


def main():
    """Main Functions"""
    left_bread, right_bread = int(input()), int(input())
    meat = "*" * ((left_bread + right_bread) * 2)
    left_bread, right_bread = "|" * left_bread, "|" * right_bread
    print("%s%s%s" % (left_bread, meat, right_bread))


main()
