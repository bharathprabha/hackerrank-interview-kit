#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the maximumToys function below.


def maximumToys(prices, k):
    heapq.heapify(prices)
    no_item = 0
    spent = 0
    while (spent <= k):
        spent = spent + heapq.heappop(prices)
        if spent <= k:
            no_item += 1
    return no_item


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
