"""Sequence V // https://ejudge.it.kmitl.ac.th/problem/8177"""


def main():
    """Main Function"""
    number = int(input())
    for _ in range(0, (number // 7)+1):
        for val_y in range(1, 8):
            if number == 0:
                break
            print(number, end=" ")
            number -= 1
            if number != 0 and val_y == 7:
                print()


main()
