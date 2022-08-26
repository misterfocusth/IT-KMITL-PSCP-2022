"""Robot I // https://ejudge.it.kmitl.ac.th/problem/8139"""


def main():
    """Main Function"""
    name = input()
    age = float(input())
    if age < 18:
        print("%s, you can pass." % name)
    else:
        print("%s, you shall not pass." % name)


main()
