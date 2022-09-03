"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ // https://ejudge.it.kmitl.ac.th/problem/8167"""


def ascend(p_1, p_2, p_3):
    """Ascending"""
    num_1, num_2, num_3 = p_1, p_2, p_3
    if p_1 > p_2:
        num_1, num_2 = num_2, num_1
    if num_2 > p_3:
        num_2, num_3 = num_3, num_2
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    print("%.2f, %.2f, %.2f" % (num_1, num_2, num_3))


def descend(p_1, p_2, p_3):
    """Descending"""
    num_1, num_2, num_3 = p_1, p_2, p_3
    if p_1 < p_2:
        num_1, num_2 = num_2, num_1
    if num_2 < p_3:
        num_2, num_3 = num_3, num_2
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    print("%.2f, %.2f, %.2f" % (num_1, num_2, num_3))


def main():
    """Main Function"""
    option = input().lower()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())

    if option == "ascend":
        ascend(num_1, num_2, num_3)
    else:
        descend(num_1, num_2, num_3)


main()
