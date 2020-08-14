#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    delete_count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            delete_count += 1
    return delete_count


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
