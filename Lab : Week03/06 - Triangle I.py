"""Triangle I // https://ejudge.it.kmitl.ac.th/problem/8158"""


def ascend(p_1, p_2, p_3):
    """Ascending"""
    num_1, num_2, num_3 = p_1, p_2, p_3
    if p_1 > p_2:
        num_1, num_2 = num_2, num_1
    if num_2 > p_3:
        num_2, num_3 = num_3, num_2
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    if abs(num_1 ** 2 + num_2 ** 2) - num_3 ** 2 > 0.01:
        print("No")
    else:
        print("Yes")


def main():
    """Triangle I"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    ascend(num_a, num_b, num_c)


main()
