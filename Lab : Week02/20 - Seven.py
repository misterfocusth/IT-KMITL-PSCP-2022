"""Seven // https://ejudge.it.kmitl.ac.th/problem/8146"""


def main():
    """Main Function"""
    number = int(input())
    if number % 4 == 1:
        print("7")
    elif number % 4 == 2:
        print("9")
    elif number % 4 == 3:
        print("3")
    elif number % 4 == 0:
        print("1")


main()
