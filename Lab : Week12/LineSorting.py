"""LineSorting"""


def main():
    """Main Function"""
    number = int(input())
    messages = []
    for _ in range(number):
        messages.append(input())
    for message in sorted(messages, key=len):
        print(message)


main()
