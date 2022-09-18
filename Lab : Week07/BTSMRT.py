"""BTS_MRT"""


def main():
    """Main Function"""
    day = input()
    age, height = float(input()), float(input())
    result = "PAY"

    if day == "Children Day":
        if age < 14 and height <= 140:
            result = "FREE"
    elif age < 14 and height < 90:
        result = "FREE"

    if day == "Senior Day":
        if age >= 60:
            result = "FREE"

    print(result)


main()
