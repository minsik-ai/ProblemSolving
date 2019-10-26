import math


def solve(p_s, q_s):
    # x = (q - p) / 2
    p_mod2s = [0, 0]
    q_mod2s = [0, 0]
    for p in p_s:
        if p % 2 == 0:
            p_mod2s[0] += 1
        else:
            p_mod2s[1] += 1
    for q in q_s:
        if q % 2 == 0:
            q_mod2s[0] += 1
        else:
            q_mod2s[1] += 1

    return p_mod2s[0] * q_mod2s[0] + p_mod2s[1] * q_mod2s[1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        dls_s = [int(r) for r in input().split(' ')]
        m = int(input())
        jls_s = [int(r) for r in input().split(' ')]
        print(solve(dls_s, jls_s))