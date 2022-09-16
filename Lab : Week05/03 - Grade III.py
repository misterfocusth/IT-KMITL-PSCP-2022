"""Grade III"""


def to_gpa(score):
    """Convert score to gpa"""
    gpa = 0
    if score >= 95 and score <= 100:
        gpa = 4
    elif score >= 90 and score < 95:
        gpa = 3.5
    elif score >= 85 and score < 90:
        gpa = 3
    elif score >= 80 and score < 85:
        gpa = 2.5
    elif score >= 75 and score < 80:
        gpa = 2
    elif score >= 70 and score < 75:
        gpa = 1.5
    elif score >= 65 and score < 70:
        gpa = 1
    elif score >= 60 and score < 65:
        gpa = 0.5
    elif score > 0 and score < 60:
        gpa = 0
    return gpa


def main():
    """Main Function"""
    number_of_subject = int(input())
    total_gpa = 0
    for _ in range(number_of_subject):
        total_gpa += to_gpa(float(input()))
    print("%.2f" % ((int((total_gpa/number_of_subject) * 100)) / 100))


main()
