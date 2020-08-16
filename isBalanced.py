#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.


def isBalanced(s):

    bracket_stack = []
    is_balanced = True
    for bracket in s:
        if bracket in ['{', '[', '(']:
            bracket_stack.append(bracket)
        elif len(bracket_stack) != 0 and match(bracket_stack[-1], bracket):
            bracket_stack.pop()
        else:
            is_balanced = False
    return 'YES' if is_balanced == True else 'NO'


def match(open_bracket, close_bracket):
    if open_bracket == "{" and close_bracket == "}":
        return True
    if open_bracket == "(" and close_bracket == ")":
        return True
    if open_bracket == "[" and close_bracket == "]":
        return True
    return False


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
