"""Squid Game 3 - Tug-of-War"""


def main():
    """Main Function"""
    player_a_1 = int(input())
    player_a_2 = int(input())
    player_a_3 = int(input())
    player_a_4 = int(input())
    player_a_5 = int(input())
    player_a_6 = int(input())
    player_a_7 = int(input())
    player_a_8 = int(input())
    player_a_9 = int(input())
    player_a_10 = int(input())
    total_a_power = player_a_1 + player_a_2 + player_a_3 + player_a_4 + \
        player_a_5 + player_a_6 + player_a_7 + player_a_8 + player_a_9 + player_a_10

    player_a_1 = int(input())
    player_a_2 = int(input())
    player_a_3 = int(input())
    player_a_4 = int(input())
    player_a_5 = int(input())
    player_a_6 = int(input())
    player_a_7 = int(input())
    player_a_8 = int(input())
    player_a_9 = int(input())
    player_a_10 = int(input())
    total_b_power = player_a_1 + player_a_2 + player_a_3 + player_a_4 + \
        player_a_5 + player_a_6 + player_a_7 + player_a_8 + player_a_9 + player_a_10

    if total_a_power == total_b_power:
        print("AB")
    elif total_a_power > total_b_power:
        print("B")
    elif total_b_power > total_a_power:
        print("A")


main()
