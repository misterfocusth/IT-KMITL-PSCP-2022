"""Meteorite"""


def main(val_a, val_b, val_c):
    """Main Function"""
    missiles_count = 0
    count = 0
    while not val_a < val_c:
        val_a = val_a / val_b
        missiles_count += (val_b ** count)
        count += 1
    print(int(missiles_count))


main(float(input()), int(input()), float(input()))
