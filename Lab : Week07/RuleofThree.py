"""Rule of Three"""


def insert_into_list(result, price, weight):
    """Insert new items into the list"""
    if len(result) != 0:
        result.clear()
    result.append(price)
    result.append(weight)


def main():
    """Main Function"""
    times = int(input())
    result = []
    current_val = 0
    for _ in range(times):
        price = float(input())
        weight = float(input())
        if result == []:
            insert_into_list(result, price, weight)
            current_val = weight / price
        if current_val > (weight / price) and current_val != 0:
            continue
        elif current_val < (weight / price) and current_val != 0:
            insert_into_list(result, price, weight)
            current_val = weight / price
        elif current_val == (weight / price) and current_val != 0:
            if result[0] > price:
                insert_into_list(result, price, weight)
    print("%.2f %.2f" % (result[0], result[1]))


main()
