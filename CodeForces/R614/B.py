def solve(n):
    hold = 0
    for s in range(1, n + 1):
        pay = 1 / s + hold
        hold = pay

    return hold


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
