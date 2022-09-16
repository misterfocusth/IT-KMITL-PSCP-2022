"""ValidVar"""


def main():
    """Main Function"""
    times = int(input())
    for _ in range(times):
        val_name = input()
        if val_name != "if" and val_name != "else" and val_name != "elif" and\
                val_name != "while" and val_name != "for" and val_name != "True" and\
                val_name != "False" and val_name != "continue" and val_name != "break" and\
                val_name != "return" and val_name != "is" and val_name != "in" and\
                val_name != "and" and val_name != "or" and val_name != "from" and\
                val_name != "as" and val_name != "pass" and val_name != "not" and\
                val_name != "def" and val_name != "None" and str(val_name).isidentifier():
            print("Valid")
        else:
            print("Invalid")


main()
