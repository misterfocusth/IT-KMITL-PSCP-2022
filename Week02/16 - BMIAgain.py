"""BMIAgain // https://ejudge.it.kmitl.ac.th/problem/8142"""


def main():
    """Main Function"""
    weight = int(input())
    height = int(input())
    height = height/100
    bmi = weight/(height**2)

    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")


main()
