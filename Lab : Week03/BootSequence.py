"""BootSequence // https://ejudge.it.kmitl.ac.th/problem/8172"""


def main():
    """Main Function"""
    num = int(input())
    for current_num in range(1, num + 1):
        if current_num == num:
            print(current_num, end="")
        else:
            print(current_num, end="_")


main()
