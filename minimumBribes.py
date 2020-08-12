#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    initial_arr = [i for i in range(1, len(q)+1)]
    swap_no = 0
    for i in range(len(q)):
        if initial_arr[i] != q[i]:
            if not q.index(q[i]) - initial_arr.index(q[i]) <= 2:
                print("Too chaotic")
                return
            else:


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
