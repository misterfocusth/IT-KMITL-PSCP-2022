"""ProgressiveTax"""


def main():
    """Main Function"""
    income = int(input())
    tax = 0

    if income > 4000000:
        over_amount = income - 4000000
        income -= over_amount
        tax += over_amount * 0.35
    if income > 2000000:
        over_amount = income - 2000000
        income -= over_amount
        tax += over_amount * 0.30
    if income > 1000000:
        over_amount = income - 1000000
        income -= over_amount
        tax += over_amount * 0.25
    if income > 750000:
        over_amount = income - 750000
        income -= over_amount
        tax += over_amount * 0.20
    if income > 500000:
        over_amount = income - 500000
        income -= over_amount
        tax += over_amount * 0.15
    if income > 300000:
        over_amount = income - 300000
        income -= over_amount
        tax += over_amount * 0.10
    if income > 150000:
        over_amount = income - 150000
        income -= over_amount
        tax += over_amount * 0.05

    print(int(tax))


main()
