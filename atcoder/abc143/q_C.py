def solve(colors):
    ans = 0
    cur = None
    for c in colors:
        if c != cur:
            cur = c
            ans += 1
            continue

    return ans


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(solve(s))
