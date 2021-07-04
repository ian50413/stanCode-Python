"""
File: predicate_function.py
Name: Jerry Liao 2020/05
-------------------------------
This program introduces predicate function
my def is_odd(n) which returns True on odd
numbers and False on even numbers
"""


def main():
    print("This program tells you if 'a' is an odd number.")
    a = int(input('a: '))
    print(is_odd(a))


def is_odd(n):
    """
    :param n: int
    :return: bool, if n is an odd number or not
    """
    return n % 2 == 1


if __name__ == '__main__':
    main()
