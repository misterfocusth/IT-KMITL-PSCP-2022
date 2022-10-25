"""AscendingSort"""


def main():
    """Main Function"""
    numbers = []
    for _ in range(5):
        numbers.append(int(input()))
    numbers = sorted(numbers)
    for number in numbers:
        print(number)


main()
