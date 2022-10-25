"""B - Fully pair"""


def main():
    """Main Function"""
    str_lists = input().lower()
    parring_lists = ""
    single_lists = ""
    for char in str_lists:
        if char not in parring_lists:
            parring_lists += char

    for char in parring_lists:
        if int(str_lists.count(char) % 2 != 0):
            single_lists += char

    if single_lists == "":
        print("fully paired")
    else:
        print(single_lists)


main()
