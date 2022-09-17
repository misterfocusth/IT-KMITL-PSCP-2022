"""SecondConverter"""


def main():
    """Main Function"""
    seconds = int(input())
    seconds_val = int(input())
    minutes_val = int(input())
    hours_val = int(input())

    result_hours = (seconds // (seconds_val * minutes_val)) % hours_val
    result_minutes = (seconds // seconds_val) % minutes_val
    result_seconds = seconds % seconds_val

    print("%d:%d:%d" % (result_hours, result_minutes, result_seconds))


main()
