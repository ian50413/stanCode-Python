"""
File: die_roll.py
Name:
---------------------
This file uses random to simulate
real die roll for shi-ba-la
"""

import random

# This constant controls the number of players for the game
NUM_PLAYER = 4


# def main():
#     """
#     This program uses random to simulate real dice roll for shi-ba-la
#     """
#     for i in range(NUM_PLAYER):
#         while True:
#             #使用while True可以先不思考終止條件
#             rolls = ''
#             for j in range(4):
#                 roll = random.randrange(1,7)
#                 rolls += str(roll)
#             if all_the_same(rolls) or two_the_same(rolls)
#             #只要有一個人true就break掉
#                 break
#             print(rolls)
#
#
# def all_the_same(rolls):
#     for i in range(1, len(rolls)):
#         if rolls[0] != rolls[i]:
#             return False
#     return True
#
#
# def two_the_same(rolls):
#     #1個一樣佩2個一樣or1個一樣佩2個不一樣
#     #判斷起來較複雜，此時用反面來思考
#     #反面：3個一樣或全部不一樣

def main():
    """
    This program uses random to simulate real dice roll for shi-ba-la
    """
    # New Version
    for i in range(NUM_PLAYER):
        while True:
            # 使用while True可以先不思考終止條件
            rolls = ''
            for j in range(4):
                roll = random.randrange(1, 7)
                rolls += str(roll)
            if all_different(rolls) or three_and_one(rolls):
                # 只要有一個人true就break掉
                pass
            else:
                break
        print(rolls)


def all_different(rolls):
    #每個人輪流當探針系列 -> double for loop
    for i in range(len(rolls)):
        for j in range(len(rolls)):
            target = rolls[i]
            if i != j:
            #不等於自己時，開始比較
                if target == rolls[j]:
                    return False
    #只要有一個不一樣即不滿足條件
    return True


def three_and_one(rolls):
    for i in range(len(rolls)):
        same_count = 0
        for j in range(len(rolls)):
            target = rolls[i]
            if i !=j:
                if target == rolls[j]:
                    same_count +=1
        if same_count == 2:
        #不包含自己故為2即有3個一樣的意思
            return True
        return False


if __name__ == '__main__':
    main()
