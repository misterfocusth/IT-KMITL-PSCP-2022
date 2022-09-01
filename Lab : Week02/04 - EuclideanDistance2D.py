"""EuclideanDistance2D // https://ejudge.it.kmitl.ac.th/problem/8130"""


def main():
    """Main Function"""
    num_q1, num_q2 = float(input()), float(input())
    num_p1, num_p2 = float(input()), float(input())
    print((((num_q1-num_p1)**2)+((num_q2-num_p2)**2))**(1/2))


main()
