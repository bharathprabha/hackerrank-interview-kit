# Uses python3
import sys

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

# return current_gcd
while(y):
    x, y = y, x % y
return x

def gcd(a, b):
    if b is 0:
        return a
    else:
        ab = a % b
    return gcd(b, ab)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
