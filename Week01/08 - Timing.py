"""Timing // https://ejudge.it.kmitl.ac.th/problem/8109"""


def main():
    """Main Functions"""
    seconds_input = int(input())
    seconds = seconds_input % 60
    minutes = (seconds_input // 60) % 60
    hours = (seconds_input // 3600) % 24
    days = seconds_input // 86400
    print("%d %d %d %d" % (days, hours, minutes, seconds))


main()
