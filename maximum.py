#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
# Complete the maximumToys function below.


def maximumToys(prices, k):
    spend = 0
    toys = 0
    for key in prices:
        if key < k and spend <= k:
            spend += key
            if spend <= k:
                toys += 1
    return toys


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
