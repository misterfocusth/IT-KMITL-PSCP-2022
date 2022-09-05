"""WeightStation // https://ejudge.it.kmitl.ac.th/problem/8157"""


def main():
    """WeightStation"""
    mean_weight = float(input())
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())
    weight_4 = (4 * mean_weight) - weight_1 - weight_2 - weight_3
    total_weight = weight_1 + weight_2 + weight_3 + weight_4

    if total_weight > 15000:
        print("Overweight")
    elif (abs(weight_1 - mean_weight) > mean_weight / 2) or \
        (abs(weight_2 - mean_weight) > mean_weight / 2) or \
            (abs(weight_3 - mean_weight) > mean_weight / 2) or \
            (abs(weight_4 - mean_weight) > mean_weight / 2):
        print("Unbalance")
    else:
        print("Pass %.2f" % (weight_4))


main()
