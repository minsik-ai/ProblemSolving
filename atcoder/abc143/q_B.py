def solve(takoyakis):
    ans = 0

    for i, x in enumerate(takoyakis):
        for j, y in enumerate(takoyakis):
            if j <= i:
                continue
            ans += x * y

    return ans


if __name__ == "__main__":
    n = int(input())
    d_s = [int(d) for d in input().split(' ')]
    print(solve(d_s))
