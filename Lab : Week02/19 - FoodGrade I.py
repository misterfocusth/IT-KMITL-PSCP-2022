"""FoodGrade I // https://ejudge.it.kmitl.ac.th/problem/8145"""


def check_and_count(current_val, weight):
    """Check is weight pass or not then return new count"""
    if weight >= 50 and weight <= 70:
        return current_val + 1
    else:
        return current_val


def main():
    """Main Function"""
    weight = int(input())
    total = check_and_count(0, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    weight = int(input())
    total = check_and_count(total, weight)

    print(total)


main()
