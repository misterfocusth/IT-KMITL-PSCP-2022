"""CompositeFunction // https://ejudge.it.kmitl.ac.th/problem/8128"""


def func_f(num_x):
    """Function f()"""
    return num_x * 2


def func_g(num_x):
    """Function g()"""
    return (num_x / 2) + 1


def main():
    """Main Function"""
    num = int(input())
    print("%.2f" % func_f(func_g(num)))
    print("%.2f" % func_g(func_f(num)))


main()
