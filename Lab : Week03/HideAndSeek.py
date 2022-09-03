"""HideAndSeek // https://ejudge.it.kmitl.ac.th/problem/8168"""


def main():
    """Main Function"""
    start, stop = int(input()), int(input())
    step = int(input())
    for current_num in range(start, stop, step):
        print(current_num)


main()
