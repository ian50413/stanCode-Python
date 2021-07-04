"""
File: average_2_nums.py
Jerry Liao 2020/05
------------------------
This file shows methods with/without parameters
as well as the return value through the concept of
stack frame
"""


def main():
    """
    This program prints the average of 10 and 9 on Console
    """
    intro()
    print('The average is: '+str(my_average(20, 78)))


def intro():
    """
    This function includes 3 prints that
    introduce the program
    """
    print('Hello! Welcome!')
    print('This program averages 10 and 9')
    print('Have fun!')


def my_average(a, b):
    """
    :param a: (int) One of the numbers that is going to be averaged
    :param b: (int) Another number that is going to be averaged
    :return ans: (float) The average of a and b
    """
    ans = (a+b)/2
    return ans


if __name__ == '__main__':
    main()
