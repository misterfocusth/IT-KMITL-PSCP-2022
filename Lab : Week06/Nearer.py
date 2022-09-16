"""Nearer"""


def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    sundaes = int(input())
    if abs(sundaes-bob) > abs(sundaes-alice):
        print("Alice", abs(sundaes-alice))
    elif abs(sundaes-bob) < abs(sundaes-alice):
        print("Bob", abs(sundaes-bob))
    elif abs(sundaes-bob) == abs(sundaes-alice):
        print("Sundaes", abs(sundaes-bob))


main()
