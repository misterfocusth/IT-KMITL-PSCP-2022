"""PointInCircle // https://ejudge.it.kmitl.ac.th/problem/8141"""


def main():
    """Main Function"""
    val_x = float(input())
    val_y = float(input())
    radius = float(input())
    circle_x = float(input())
    circle_y = float(input())

    if ((val_x - circle_x) ** 2) + ((val_y - circle_y) ** 2) <= radius ** 2:
        print("True")
    else:
        print("False")


main()
