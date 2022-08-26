"""Timing // https://ejudge.it.kmitl.ac.th/problem/8134"""


def main():
    """Timing"""
    sec = int(input())
    minx = sec // 60
    sec = sec % 60
    hour = minx // 60
    minx = minx % 60
    day = hour // 24
    hour = hour % 24
    if day > 9999:
        return print("ERR_:__:__:__")
    print("%04d:%02d:%02d:%02d" % (day, hour, minx, sec))


main()
