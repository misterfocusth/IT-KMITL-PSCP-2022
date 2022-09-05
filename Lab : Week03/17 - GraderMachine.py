"""GraderMachine // https://ejudge.it.kmitl.ac.th/problem/8169"""


def main():
    """Main Function"""
    start, stop = int(input()), int(input())
    total = 0

    print("pass :", end=" ")

    if start > stop:
        for current_num in range(start, (stop - 1), -1):
            if current_num % 2 == 0:
                total += current_num
                print("%d" % current_num, end=" ")

    for current_num in range(start, stop + 1):
        if current_num % 2 == 0:
            total += current_num
            print("%d" % current_num, end=" ")

    print()
    print("Sum : %d" % total)


main()
