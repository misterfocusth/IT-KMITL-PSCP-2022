"""ODD_EVEN // https://ejudge.it.kmitl.ac.th/problem/8136"""


def is_odd(num_x):
    """Check is odd"""
    return True if num_x % 2 != 0 else False


def main():
    """Main Function"""
    num = int(input())
    return print("True") if is_odd(num) == True else print("False")


main()
