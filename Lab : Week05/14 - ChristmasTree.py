"""ChristmasTree"""


def main():
    """Main Function"""
    value_n = int(input())
    value_k = int(input())
    for value_i in range(1, value_n + 1):
        print(" " * (value_n - value_i), end="")  # ช่องว่าง
        print("*" * (value_i * 2 - 1))  # ดาว
    for _ in range(value_k):
        print(" " * (value_n - 2), end="")
        print("---")


main()
