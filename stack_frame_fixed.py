"""
File: stack_frame_fixed.py
Jerry Liao 2020/05
------------------------
This file shows the concept of parameter passing
through stack frames
"""


def main():
    print('-------------')
    a = 0
    a = plus_one(a)
    print(a)
    print('-------------')


def plus_one(a):
    a += 1
    return a


if __name__ == '__main__':
    main()
