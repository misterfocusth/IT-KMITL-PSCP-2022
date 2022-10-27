"""Frame"""


def main():
    """Main Function"""
    message = input()
    print("*" * (len(message) + 2))
    print("%s%s%s" % ("*", message, "*"))
    print("*" * (len(message) + 2))


main()
