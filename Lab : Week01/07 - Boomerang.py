"""Boomerang // https://ejudge.it.kmitl.ac.th/problem/8108"""


def main():
    """Main Functions"""
    number_x = int(input())
    number_y = int(input())
    number_z = int(input())
    print(number_x + 1)
    print((7*(number_y**3)) + (2*(number_y**2) - (31*number_y) + 1))
    print(-number_z)
    print((number_x + number_y) * (number_x - number_y))
    top = number_y - (number_y**2 - 4 * number_x * number_z)**0.5
    bottom = 2 * number_x
    print(top / bottom)


main()
