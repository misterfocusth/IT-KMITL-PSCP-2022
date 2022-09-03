"""Day I // https://ejudge.it.kmitl.ac.th/problem/8153"""


def is_leap(year):
    """Return true if input year is leap year"""
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True


def main():
    """Main Function"""
    year = int(input())
    if is_leap(year):
        print("Yes")
    else:
        print("No")


main()
