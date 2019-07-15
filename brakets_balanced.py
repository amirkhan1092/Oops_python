# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.

def brakets_balance(s):
    round = 0
    curly = 0
    square = 0
    for i in s:
        if i == '(':
            round += 1
        elif i == '[':
            square += 1
        elif i == '{':
            curly += 1

        elif i == ')':
            round -= 1
        elif i == ']':
            square -= 1
        elif i == '}':
            curly -= 1

        if round < 0 or curly < 0 or square < 0:
            return False


    else:
        if round == curly == square == 0:
            return True
        else:
            return False


s = input('enter the srring pattern of brakets ')
print(brakets_balance(s))