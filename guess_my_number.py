"""
File: guess_my_number.py
Name:Ian Chen
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""
# 常數用單行註解敘述一下
# This number controls when to stop the game
SECRET = 78



# def main():
#     """
#     Ver新手版本 guess input*2
#     """
#     print('Guess a number from 0-99!')
#     guess=int(input('Your Guess'))
#
#     while guess!=SECRET:
#         if guess>SECRET:
#             print('Too High!')
#             guess=int(input('Your Guess:'))
#         else:
#             print('Too Low!')
#             guess=int(input('Your Guess:'))
#     print('Congrats')

# def main():
#     """
#     Ver精簡 guess input只輸入一次
#     """
#     print('Guess a number from 0-99!')
#     guess=int(input('Your Guess'))
#
#     while guess!=SECRET:
#         if guess>SECRET:
#             print('Too High!')
#         else:
#             print('Too Low!')
#         guess=int(input('Your Guess:'))
#     print('Congrats')


# def main():
#     """
#     while True Ver1.(V1,V2差在elif設定不同) if->elif(複數個可行)->else絕對的順序
#     """
#     print('Guess a number from 0-99!')
#     while True:
#         guess=int(input('Your Guess:'))
#         if guess>SECRET:
#             print('Too Big!')
#         elif guess==SECRET:
#             break
#         else:
#             print('Too Low!')
#
#     print('Congrats!')


def main():
    """
    while True Ver2.
    """
    print('Guess a number from 0-99!')
    while True:
        guess = int(input('Your Guess:'))
        if guess > SECRET:
            print('Too Big!')
        elif guess < SECRET:
            print('Too Low!')
        else:
            break

    print('Congrats!')

### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
