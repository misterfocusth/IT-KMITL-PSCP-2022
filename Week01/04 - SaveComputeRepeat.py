"""SaveComputeRepeat // https://ejudge.it.kmitl.ac.th/problem/8105"""


def main():
    """Main Functions"""
    start_here = 492137954293754252786
    milliseconds = start_here
    seconds = milliseconds // 1000
    milliseconds = milliseconds % 1000
    minuets = seconds // 60
    seconds = seconds % 60
    hours = minuets // 60
    minuets = minuets % 60
    days = hours // 24
    hours = hours % 24
    print("%d %d %d %d %d" % (days, hours, minuets, seconds, milliseconds))


main()
