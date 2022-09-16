"""Run Length Encoding"""


def main():
    """Main Function"""
    raw_string = input()
    encoded_msg = ""
    current_char = ""
    char_count = 0
    for string in raw_string:
        if current_char == "":
            current_char = string
            char_count += 1
        elif current_char == string:
            char_count += 1
        elif current_char != string:
            encoded_msg += str(char_count) + current_char
            current_char = string
            char_count = 1
    encoded_msg += str(char_count) + current_char
    print(encoded_msg)


main()
