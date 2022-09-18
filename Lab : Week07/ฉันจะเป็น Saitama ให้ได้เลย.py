"""Docstring"""


def main():
    """Main Function"""
    val_a = int(input())
    val_b = int(input())
    val_c = int(input())
    val_d = int(input())

    val_a_day = int(input())
    val_b_day = int(input())
    val_c_day = int(input())
    val_d_day = int(input())

    mission_1_days = val_a / val_a_day
    mission_2_days = val_b / val_b_day
    mission_3_days = val_c / val_d_day
    mission_4_days = val_d / val_c_day

    for _ in range(4):  # Manual Bubble Sort
        if mission_1_days <= mission_2_days:
            mission_1_days, mission_2_days = mission_2_days, mission_1_days
        if mission_2_days <= mission_3_days:
            mission_2_days, mission_3_days = mission_3_days, mission_2_days
        if mission_3_days <= mission_4_days:
            mission_3_days, mission_4_days = mission_4_days, mission_3_days

    print(int(mission_1_days + 0.999999999))


main()
