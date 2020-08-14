#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):
    pos_arr = [abs(i) for i in arr]
    heapq.heapify(pos_arr)
    first_least = heapq.heappop(arr)
    second_least = heapq.heappop(arr)

    min_difference = abs(first_least - second_least)

    return min_difference


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
