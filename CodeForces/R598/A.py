def solve(a, b, n, S):
    div = S // n
    if div > a:
        div = a
    if (S - div * n) <= b:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        a, b, n, S = [int(r) for r in input().split(' ')]
        print(solve(a, b, n, S))
