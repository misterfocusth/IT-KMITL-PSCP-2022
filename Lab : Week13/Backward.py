"""Backward"""


def main():
    """Main Function"""
    messages = []
    while True:
        message = input()
        if message == "NULL":
            break
        else:
            messages.append(message)
    messages.reverse()
    print(* messages, sep="\n")


main()
