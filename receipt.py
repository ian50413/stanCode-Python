"""
File: receipt.py
Name: Ian Chen
-------------------------
This program calculates the meal cost
and prints the result on Console.
Students will learn variables, user inputs,
and concatenation
"""


def main():
    meal=int(input('How much was your meal? '))
    tax=float(input('Tax? '))
    total=meal*tax
    print('Total: '+str(meal+total)+'!')


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
