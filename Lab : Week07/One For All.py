"""One For All"""


def main():
    """Main Function"""
    val_n = int(input())
    count = 0
    result = ""
    for val_x in range(1, val_n + 1):
        name = input()
        count += 1

        if val_x == val_n:
            result += (name + "_%d" % count)
        elif val_x % 2 == 0:
            result += (name + "-" * val_x)
        else:
            result += (name + "*" * val_x)

    print(result)


main()
