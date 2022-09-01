"""Quadrant // https://ejudge.it.kmitl.ac.th/problem/8138"""


def main():
    """Main Function"""
    num_x = int(input())
    num_y = int(input())
    if num_x > 0 and num_y > 0:
        print("Q1")
    elif num_x < 0 and num_y > 0:
        print("Q2")
    elif num_x < 0 and num_y < 0:
        print("Q3")
    elif num_x > 0 and num_y < 0:
        print("Q4")
    elif num_x == 0 and num_y == 0:
        print("O")
    elif num_y == 0:
        print("X")
    elif num_x == 0:
        print("Y")


main()
