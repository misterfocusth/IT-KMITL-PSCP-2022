"""Netflix"""


def display_package(premium, standard, basic, mobile, total):
    """Display netflix's package"""
    if premium > 0:
        print("Premium x %d" % premium)
    if standard > 0:
        print("Standard x %d" % standard*(standard > 0))
    if basic > 0:
        print("Basic x %d" % basic*(basic > 0))
    if mobile > 0:
        print("Mobile x %d" % mobile*(mobile > 0))
    print("Total = %d THB" % total)


def main():
    """Main Function"""
    numbers_of_screen = int(input())
    numbers_of_phone = int(input())
    input()
    input()
    watch_on_laptop_tv = input().lower()
    hd_available = input().lower()
    ultra_available = input().lower()

    premium_count = 0
    standard_count = 0
    basic_count = 0
    mobile_count = 0
    total = 0

    while numbers_of_screen > 0 or numbers_of_phone > 0:
        if (ultra_available == "yes" or hd_available == "yes" or watch_on_laptop_tv == "yes") \
                and (numbers_of_screen >= 3 or numbers_of_phone >= 3):
            total += 419
            premium_count += 1
            numbers_of_screen -= 4
            numbers_of_phone -= 4
        elif (hd_available == "yes" or watch_on_laptop_tv == "yes") \
                and (numbers_of_screen >= 2 or numbers_of_phone >= 2):
            total += 349
            standard_count += 1
            numbers_of_screen -= 2
            numbers_of_phone -= 2
        elif watch_on_laptop_tv == "yes" and ultra_available == "no" and hd_available == "no":
            total += 279
            basic_count += 1
            numbers_of_screen -= 1
            numbers_of_phone -= 1
        else:
            if ultra_available == "yes":
                total += 419
                premium_count += 1
                numbers_of_screen -= 4
                numbers_of_phone -= 4
            elif hd_available == "yes":
                total += 349
                standard_count += 1
                numbers_of_screen -= 2
                numbers_of_phone -= 2
            elif watch_on_laptop_tv == "yes":
                total += 279
                basic_count += 1
                numbers_of_screen -= 1
                numbers_of_phone -= 1
            else:
                total += 99
                mobile_count += 1
                numbers_of_screen -= 1
                numbers_of_phone -= 1
    display_package(premium_count, standard_count,
                    basic_count, mobile_count, total)


main()
