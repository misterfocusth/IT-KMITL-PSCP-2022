"""Restaurant"""


def restaurant(current_price, promo_price, discount, offer):
    """Restaurant"""
    total = current_price + offer
    if current_price + offer >= promo_price:
        total -= (current_price + offer) * (discount / 100)

    if current_price >= promo_price:
        current_price -= current_price * (discount / 100)

    if (current_price + offer) > current_price:
        print("No %.03f" % ((current_price + offer) - current_price))
    elif (current_price + offer) < current_price:
        print("Yes %.03f" % (current_price - (current_price + offer)))
    else:
        print("Yes")


restaurant(float(input()), float(input()), float(input()), float(input()))
