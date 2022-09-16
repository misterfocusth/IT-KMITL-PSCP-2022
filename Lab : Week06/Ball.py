"""Ball"""


def main():
    """Main Function"""
    height = float(input())
    total_times = 0
    while True:
        value_x = height / 5 * 3
        if value_x > 0.01:
            total_times += 1
            height = value_x
        else:
            break
    print(total_times)


main()
