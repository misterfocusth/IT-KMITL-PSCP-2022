"""SaveComputeRepeat // https://ejudge.it.kmitl.ac.th/problem/8105"""


def main():
    """Main Functions"""
    milliseconds = 492137954293754252786
    seconds = milliseconds // 1000
    milliseconds %= 1000
    minuets = seconds // 60
    seconds %= 60
    hours = minuets // 60
    minuets %= 60
    days = hours // 24
    hours %= 24
    print("%d %d %d %d %d" % (days, hours, minuets, seconds, milliseconds))


main()
