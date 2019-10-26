def solve(n, a_s):
    a_set = set(a_s)
    for a in a_s:
        if a > 1 and (a - 1) in a_set:
            return 2
        if a < 100 and (a + 1) in a_set:
            return 2
    return 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_s = [int(r) for r in input().split(' ')]
        print(solve(n, a_s))
