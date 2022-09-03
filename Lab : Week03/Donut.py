"""Donut // https://ejudge.it.kmitl.ac.th/problem/8160"""


def main():
    """Main Function"""
    donut_price = int(input())
    donut_qty_cont = int(input())
    donut_qty_promotion = int(input())
    buy_amount = int(input())

    current_donut_qty = 0
    promotion_qty = donut_qty_cont + donut_qty_promotion
    amount = buy_amount // promotion_qty

    if buy_amount <= 0:
        return print("0 0")
    if buy_amount > 0:
        current_donut_qty = amount * promotion_qty
        missing = buy_amount - current_donut_qty
        if missing > amount:
            missing = amount
        if missing >= amount:
            current_donut_qty += promotion_qty
        else:
            current_donut_qty += missing

    print("%d %d" % ((donut_price*amount*donut_qty_cont) +
          (missing*donut_price), current_donut_qty))


main()
