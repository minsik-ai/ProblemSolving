import math


def solve(n, d, platforms):
    m = len(platforms)
    waters = n - sum(platforms)
    max_dist = math.ceil(waters / (m + 1)) + 1
    if max_dist > d:
        print("NO")
        return
    ans = [0] * n

    dist = max_dist - 1
    left = sum(platforms)
    cur_i = 0
    for i, c in enumerate(platforms):
        if left <= n - cur_i:
            dist = 0
        cur_i += dist
        for j in range(cur_i, cur_i + c):
            ans[j] = i + 1
        cur_i += c
        left -= c
    print('YES')
    print(' '.join([str(e) for e in ans]))


if __name__ == "__main__":
    n, m, d = [int(r) for r in input().split(' ')]
    platforms = [int(r) for r in input().split(' ')]
    solve(n, d, platforms)
