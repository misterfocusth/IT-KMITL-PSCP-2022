"""Cat Parade"""


def main():
    """Main Function"""
    all_cats = []
    unique_cats = []
    while True:
        new_cat = input()
        if new_cat == "END":
            break
        elif new_cat != "IT'S A DOG":
            new_cat = new_cat.split(",")
            for cat in new_cat:
                all_cats.append(cat.strip())
                if cat.strip() not in unique_cats:
                    unique_cats.append(cat.strip())
        elif new_cat == "IT'S A DOG":
            all_cats.pop()
            unique_cats.pop()
    unique_cats.sort()

    for cat in unique_cats:
        print(cat, all_cats.index(cat) + 1, all_cats.count(cat))


main()
