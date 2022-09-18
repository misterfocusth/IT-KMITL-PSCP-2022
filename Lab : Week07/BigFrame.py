"""BigFrame"""


def main():
    """Main Function"""
    line_1 = input().rstrip()
    line_2 = input().rstrip()
    line_3 = input().rstrip()
    line_4 = input().rstrip()
    line_5 = input().rstrip()
    max_length = max(len(line_1), len(line_2), len(
        line_3), len(line_4), len(line_5))

    print("*" * (max_length + 4))
    print("%s %s %s%s" % ("*", line_1, (" " * (max_length - len(line_1))), "*"))
    print("%s %s %s%s" % ("*", line_2, (" " * (max_length - len(line_2))), "*"))
    print("%s %s %s%s" % ("*", line_3, (" " * (max_length - len(line_3))), "*"))
    print("%s %s %s%s" % ("*", line_4, (" " * (max_length - len(line_4))), "*"))
    print("%s %s %s%s" % ("*", line_5, (" " * (max_length - len(line_5))), "*"))
    print("*" * (max_length + 4))


main()
