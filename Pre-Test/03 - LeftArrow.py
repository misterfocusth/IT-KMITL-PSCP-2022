"""[Pre] LeftArrow / https://ejudge.it.kmitl.ac.th/problem/8099"""


def main():
    """Main Functions"""
    long, height = int(input()), int(input())
    space, space_idx = " ", int(height / 2)
    is_half = False
    for _ in range(height):
        if space_idx == 0:
            is_half = True

        if is_half:
            print("%s%s" % ((space * space_idx), "*" * long))
            space_idx += 1
        else:
            print("%s%s" % ((space * space_idx), "*" * long))
            space_idx -= 1


main()
