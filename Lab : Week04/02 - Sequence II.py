"""Sequence II // https://ejudge.it.kmitl.ac.th/problem/8175"""


def main():
    """Main Function"""
    times = int(input())
    for current_num in range(1, times + 1, 1):
        if current_num != (times + 1):
            print(current_num ** 2, end=" ")
        else:
            print(current_num ** 2)


main()
