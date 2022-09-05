"""BrickBridge // https://ejudge.it.kmitl.ac.th/problem/8162"""


def main():
    """Main Function"""
    brick_a = int(input())
    brick_b = int(input())
    goal = int(input())

    if goal % 5 > brick_a or (brick_a + (brick_b * 5)) < goal:
        print(-1)
    else:
        if brick_b * 5 >= goal:
            result = goal % 5
        else:
            result = goal-(brick_b*5)
        print(result)


main()
