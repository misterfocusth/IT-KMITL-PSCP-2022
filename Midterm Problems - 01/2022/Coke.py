"""Coke"""


def main(val_a, val_b, val_c, val_d):
    """Main Function"""
    if val_b == 0:
        return print(val_d * val_a)
    else:
        discounted_cokes = val_d // val_b
        val_d -= discounted_cokes
        total_price = (val_d * val_a) + (discounted_cokes * val_c)
        print(int(total_price))


main(float(input()), float(input()), float(input()), float(input()))
