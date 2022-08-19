"""MyMath // https://ejudge.it.kmitl.ac.th/problem/8112"""

import math

def main():
    """Main Functions"""
    top = math.sin(math.radians(90)) + math.sin(math.radians(60))**2
    bottom = math.cos(math.radians(245**2)) + math.cos(math.radians(45+135))
    print(top / bottom)
    print((math.factorial(16) * math.factorial(4)) / math.factorial(8))
    print((15+25) / math.sqrt((25-12)**2 + (12-15)**2))
    print(math.log(1234**4, 10))
    top = math.log(4234, 5) + math.log(8191, 2) + 71*math.log(156154, 10)
    bottom = math.log(777, 7) - math.log(888, 8) - math.log(999, 9)
    print(top/bottom)


main()
