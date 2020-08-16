#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.


def luckBalance(k, contests):
    max_luck = 0
    contests.sort(reverse=True)
    print(contests)
    for key in contests:
        if key[1] == 1 and k > 0:
            max_luck += key[0]
            k -= 1
        elif key[1] == 1 and k == 0:
            max_luck -= key[0]
        else:
            max_luck += key[0]

    return max_luck


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)
