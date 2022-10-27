"""Volleyball"""


def compare_winner(stats_winner_team_a, stats_winner_team_b, value):
    """Compare winner stats between team a and team b"""
    return stats_winner_team_a >= value or stats_winner_team_b >= value


def is_not_deal_mode(stats_winner_team_a, stats_winner_team_b):
    """Check is deal mode or not"""
    return abs(stats_winner_team_a - stats_winner_team_b) >= 2


def main():
    """Main Function"""
    value = input() + " "
    stat_win_a = 0
    stat_win_b = 0
    stat_round_a = 0
    stat_round_b = 0
    string_builder = ""
    increment = 0
    finished = False
    while len(value) != 0:
        for text in value:
            if compare_winner(stat_win_a, stat_win_b, 25) \
                    and is_not_deal_mode(stat_win_a, stat_win_b) and increment <= 3:
                finished = True
                break
            if compare_winner(stat_win_a, stat_win_b, 15) \
                    and is_not_deal_mode(stat_win_a, stat_win_b) and increment == 4:
                finished = True
                break
            if text == "A":
                stat_win_a = stat_win_a + 1
            elif text == "B":
                stat_win_b = stat_win_b + 1
            string_builder = string_builder + text
        increment = increment + 1
        if stat_win_a > stat_win_b:
            stat_round_a = stat_round_a + 1
        else:
            stat_round_b = stat_round_b + 1
        if increment <= 5:
            print("Set %d: A (%d) | B (%d)" %
                  (increment, stat_win_a, stat_win_b))
        value = value.replace(string_builder, "", 1)
        if increment >= 4 and finished and stat_round_a-stat_round_b != 0 \
                or (abs(stat_round_a-stat_round_b) == 3):
            print("A won %d:%d set"
                  % (stat_round_a, stat_round_b)*(stat_round_a > stat_round_b) +
                  "B won %d:%d set"
                  % (stat_round_b, stat_round_a)*(stat_round_a < stat_round_b))
            break
        finished = False
        stat_win_a = 0
        stat_win_b = 0
        string_builder = ""
    if not finished:
        print("The game has not finished yet.")


main()
