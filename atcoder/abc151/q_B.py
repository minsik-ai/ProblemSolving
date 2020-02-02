def solve(n, k, m, a_s):
    ans = n * m - sum(a_s)
    if ans > k:
        return -1
    if ans < 0:
        return 0
    return ans


if __name__ == "__main__":
    raw = input()
    a_s = input()
    n, k, m = [int(r) for r in raw.split(' ')]
    a_s = [int(r) for r in a_s.split(' ')]
    print(solve(n, k, m, a_s))
