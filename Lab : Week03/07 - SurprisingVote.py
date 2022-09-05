"""SurprisingVote // https://ejudge.it.kmitl.ac.th/problem/8159"""


def main():
    """Main Function"""
    total_score = float(input())
    highest_score = float(input())
    val_z = 0
    if highest_score * 2 < total_score:
        val_z = total_score - highest_score * 2
    if highest_score - val_z > 2:
        print("Surprising")
    else:
        print("Not surprising")


main()
