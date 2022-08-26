"""BMI // https://ejudge.it.kmitl.ac.th/problem/8127"""


def cal_bmi():
    """Calculate BMI value"""
    name = input()
    weight = float(input())
    height = float(input())
    height = height/100
    bmi = weight/(height**2)
    print("%s's  BMI = %.2f" % (name, bmi))


def main():
    """Main Function"""
    cal_bmi()
    cal_bmi()
    cal_bmi()
    cal_bmi()
    cal_bmi()


main()
