"""PhoneNumber"""


def main():
    """Main Function"""
    phone_number = input()
    number_type = input()
    formatted_number = "+66" if number_type == "International" else "0"
    for index in range(len(phone_number) - 1, 0, -1):
        if index % 4 == 0:
            formatted_number += (" " + phone_number[len(phone_number) - index])
        else:
            formatted_number += phone_number[len(phone_number) - index]

    print(formatted_number)


main()
