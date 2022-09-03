"""Circular I // https://ejudge.it.kmitl.ac.th/problem/8154"""


def main():
    """Main Function"""
    val_x1 = float(input())
    val_x2 = float(input())
    radius = float(input())
    val_y1 = float(input())
    val_y2 = float(input())
    result = (((val_x1 - val_y1) ** 2) + ((val_x2 - val_y2) ** 2)) ** 0.5
    return print("Yes") if (result <= radius) else print("No")


main()
