"""HowLong // https://ejudge.it.kmitl.ac.th/problem/8171"""


def main():
    """Main Function"""
    num = abs(int(input().strip()))
    result = 0
    for _ in str(num):
        result += 1
    print(result)


main()
