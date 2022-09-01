"""DataSpike // https://ejudge.it.kmitl.ac.th/problem/8144"""


def compare(current_val, new_val):
    """Compare current and new value and return result"""
    if new_val > current_val:
        return new_val
    else:
        return current_val


def main():
    """Main Function"""
    new_value = int(input())
    result = compare(0, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    new_value = int(input())
    result = compare(result, new_value)

    print(result)


main()
