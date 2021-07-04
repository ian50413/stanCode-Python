"""
File: find_max.py
Name:Ian Chen
--------------------------
This program finds the maximum among
all user inputs. Students can refer to
this file when they are doing Problem 2
in Assignment 2
"""

# This constant controls when to stop
EXIT = 100


def main():
    """
    This program find the maximum among
    user inputs
    """
    print('This program finds the maximum.')
    data = int(input('Data:'))
    if data == EXIT:
        print('No numbers were entered')
    else:
        maximum = data
        while True:
            data = int(input('Data:'))
            # 下述兩個if顛倒會完全影響過程，應該先data==EXIT作為SENTINEL來先判斷是否該終止
            # 否則SENTINEL會被作為其中一個DATA然後完全COVER掉result
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print('Maximum:'+str(maximum))



### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
