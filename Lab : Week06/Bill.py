"""Bill"""


def main():
    """Bill"""
    price = float(input())
    service_charge = price * 10 / 100
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    price += service_charge
    price = price * 107 / 100
    print("%.2f" % (price))


main()
