"""[Pre] Blackjack / https://ejudge.it.kmitl.ac.th/problem/8100"""


def main():
    """Main Functions"""
    card_qty = int(input())
    cards, a_cards = [], []
    for _ in range(card_qty):
        new_card = input()
        if new_card == "A":
            a_cards.append("A")
        elif new_card.isdigit():
            cards.append(int(new_card))
        elif "JQK".count(new_card) == 1:
            cards.append(10)
    for _ in range(len(a_cards)):
        a_cards.remove("A")
        if sum(cards) + 11 > 21:
            cards.append(1)
        elif sum(cards) == 10 and len(a_cards) == 1:
            cards.append(1)
        else:
            cards.append(11)
    print(sum(cards))


main()
