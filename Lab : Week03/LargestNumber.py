"""LargestNumber // https://ejudge.it.kmitl.ac.th/problem/8161"""


def main():
    """Main Function"""
    num_1, num_2, num_3 = int(input()), int(input()), int(input())

    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    if num_2 < num_3:
        num_2, num_3 = num_3, num_2
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    print(num_1, num_2, num_3, sep="")


main()
