import collections

def solve(segs, k):
    covered = [0 for _ in range(200)]
    for l, r in segs:
        for i in range(l, r + 1):
            covered[i] += 1
    seg_map = {}
    for l, r in segs:
        cnt = 0
        for i in range(l, r + 1):
            if covered[i]:
                cnt += 1
        seg_map[(l, r)] = cnt
    while True:


if __name__ == "__main__":
    n, k = [int(s) for s in input().split(' ')]
    segs = [input().split(' ') for _ in range(n)]
    solve(segs, k)
