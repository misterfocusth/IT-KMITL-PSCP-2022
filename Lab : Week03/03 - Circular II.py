"""Circular II // https://ejudge.it.kmitl.ac.th/problem/8155"""


def main():
    """Main Function"""
    val_x1 = float(input())
    val_x2 = float(input())
    radius_1 = float(input())
    val_y1 = float(input())
    val_y2 = float(input())
    radius_2 = float(input())
    result = (((val_x1 - val_y1) ** 2) + ((val_x2 - val_y2) ** 2)) ** 0.5
    return print("Yes") if (radius_1 + radius_2) > result else print("No")


main()
