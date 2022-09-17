"""Turnstile"""


def main():
    """Main Function"""
    entry_count = 0
    is_unlocked = False
    while True:
        state = input()
        if state == "END":
            break
        if state == "C":
            is_unlocked = True
        elif state == "P" and is_unlocked == True:
            entry_count += 1
            is_unlocked = False
    print(entry_count)


main()
