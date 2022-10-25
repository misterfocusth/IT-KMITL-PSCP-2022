"""diamond"""


def main():
    """Main Function"""
    number = int(input())
    half_val = number // 2
    for i in range(number):
        for j in range(number):
            if i == half_val or i + j == half_val or j - i == half_val or i - j == half_val or\
                    j == number - i + half_val - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


main()
