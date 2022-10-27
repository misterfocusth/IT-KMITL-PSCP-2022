"""Heron of Alexandria"""

import math


def main(val_a, val_b, val_c):
    """Main Function"""
    val_s = (val_a + val_b + val_c) / 2
    area = math.sqrt((val_s * (val_s - val_a)
                      * (val_s - val_b) * (val_s - val_c)))
    print("%.3f" % area)


main(float(input()), float(input()), float(input()))
