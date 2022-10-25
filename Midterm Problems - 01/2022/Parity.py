"""Parity"""


def main(string, message):
    """Main Function"""
    one_count = 0
    for val_x in string:
        if val_x == "1":
            one_count += 1
    if one_count % 2 == 0:
        if message == "Even":
            string += "0"
        elif message == "Odd":
            string += "1"
    elif one_count % 2 == 1:
        if message == "Even":
            string += "1"
        elif message == "Odd":
            string += "0"
    print(string)


main(input(), input())
