"""Run Length Decoding"""


def main():
    """Main Function"""
    encoded_msg = input()
    multiplier = ""
    for string in encoded_msg:
        if string.isnumeric():
            multiplier += string
        else:
            print(string * int(multiplier), end="")
            multiplier = ""


main()
