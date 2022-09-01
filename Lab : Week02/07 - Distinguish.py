"""Distinguish // https://ejudge.it.kmitl.ac.th/problem/8133"""


def main():
    """Main Function"""
    height = int(input())
    return print("You're hit the door edge.") if height > 180 else print("Nothing happens.")


main()
