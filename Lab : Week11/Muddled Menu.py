"""Muddled Menu"""


def main():
    """Main Function"""
    full_course = []
    reversed = []
    while True:
        menu = input()

        if menu == "SOMETHING'S WRONG":
            full_course.clear()
            continue
        elif menu == "DONE" or menu == "CLOSED":
            break

        if "#" in menu:
            menu = menu.split("#")
            if menu[1] != "N":
                full_course.insert(int(menu[1]), menu[0].strip())
            else:
                full_course.append(menu[0].strip())

        if "Can't do" in menu:
            menu = menu.replace("Can't do: ", "")
            target_idx = full_course.index(menu.strip())
            full_course.pop(target_idx)

    reversed = sorted(full_course, reverse=True)
    print("Full Course:", full_course, end=" ")
    print("Reversed:", reversed)


main()
