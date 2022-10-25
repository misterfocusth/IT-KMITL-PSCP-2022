"""Calculator"""


def main(number):
    """Main Function"""
    count = 0
    if number == 1:
        return print("1")
    else:
        for val_x in range(1, number + 1, 1):
            count += (len(str(val_x)) + 1)
    print(count)


main(int(input()))
