"""
File: my_smaller.py
Name:Ian Chen
-------------------------
This program implements a min function
which takes 2 arguments and outs the
smaller one
"""


def main():
    """
    Call my_min function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)


def my_smaller(n1, n2):
    """
    :param n1: int, the number to be compared
    :param n2: int, the number to be compared
    :return: int, the smaller one between n1 and n2
    """
    if n1<n2:
        return n1
    return n2


if __name__ == '__main__':
    main()
