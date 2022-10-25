"""Restaurant"""


from audioop import add


def main():
    """Main Function"""
    current_price = float(input())
    promotion_price = float(input())
    promotion_discount_percent = float(input())
    additional_price = float(input())

    if current_price + additional_price >= promotion_price:
        pay_with_offer = (current_price + additional_price) * \
            (100 - promotion_discount_percent)


main()
