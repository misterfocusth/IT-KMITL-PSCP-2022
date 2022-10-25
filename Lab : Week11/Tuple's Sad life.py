"""Tuple's Sad life"""


def main(numbers, target_number):
    """Main Function"""

    for _ in range(numbers.count(target_number)):
        for _ in range(numbers.count(target_number)):
            print(numbers.index(target_number), end=" ")
        print()


main(tuple(input().split(" ")), input())
