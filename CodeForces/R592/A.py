# a lectures
# b classes

# c lectures per pen
# d classes per pencil

# x pens, y pencils, x + y <= k

# t test cases
# 1 <= a, b, c, d, k <= 100

# -1 or "x y"

import math


def solve(a, b, c, d, k):
    x = math.ceil(a / c)
    y = math.ceil(b / d)
    if x + y > k:
        return "-1"
    else:
        return f"{x} {y}"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d, k = [int(r) for r in input().split(' ')]
        print(solve(a, b, c, d, k))