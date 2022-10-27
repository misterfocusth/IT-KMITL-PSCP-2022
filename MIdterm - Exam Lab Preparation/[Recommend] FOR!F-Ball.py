"""FOR!F-Ball"""


def main():
    """Main Function"""
    data = input()
    result = 1
    for case in data:
        if case == "A":
            if result == 1:
                result = 2
            elif result == 2:
                result = 1
        elif case == "B":
            if result == 2:
                result = 3
            elif result == 3:
                result = 2
        elif case == "C":
            if result == 3:
                result = 1
            elif result == 1:
                result = 3
    print(result)


main()
