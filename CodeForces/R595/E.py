import math


def solve(n, c, a_s, b_s):
    ans = [math.inf for _ in range(n)]
    a_cul, b_cul = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
    for i, a in enumerate(a_s):
        a_cul[i + 1] = a_cul[i] + a
    for i, b in enumerate(b_s):
        b_cul[i + 1] = b_cul[i] + b

    ans[0] = 0
    for i in range(1, n):
        ans[i] = min([ans[j] + min(a_cul[i] - a_cul[j], c + b_cul[i] - b_cul[j]) for j in range(0, i)])

    return ' '.join([str(i) for i in ans])


if __name__ == "__main__":
    n, c = [int(k) for k in input().split(' ')]
    a_s = [int(a) for a in input().split(' ')]
    b_s = [int(b) for b in input().split(' ')]
    print(solve(n, c, a_s, b_s))
