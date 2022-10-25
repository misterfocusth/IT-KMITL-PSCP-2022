"""MissingNumber"""


def main():
    """Main Function"""
    times = int(input())
    missing_numbers = []
    for val_x in range(times + 1):
        missing_numbers.append(val_x)
    for _ in range(times):
        new_num = int(input())
        missing_numbers.remove(new_num)
        if new_num == 0:
            break
    missing_numbers = sorted(missing_numbers)
    for val_x in missing_numbers:
        print(val_x)


main()
