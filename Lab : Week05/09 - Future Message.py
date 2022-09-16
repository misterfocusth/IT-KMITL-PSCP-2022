"""Future Message"""


def main():
    """Main Function"""
    message = input()
    if message.isdecimal():
        print("Number")
    elif message.isupper():
        print("Uppercase")
    elif message.islower():
        print("Lowercase")
    elif message.istitle():
        print("Title")
    elif message.isspace():
        print("Space")
    else:
        print("Other")


main()
