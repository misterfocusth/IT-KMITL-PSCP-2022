"""SumOfNumber // https://ejudge.it.kmitl.ac.th/problem/8170"""


def main():
    """Main Function"""
    stop_val = int(input())
    total = 0
    while True:
        num = int(input())
        if num < 0:
            break
        else:
            total += num
        if total == stop_val:
            break
    print(total)


main()
