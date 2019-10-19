def solve(rooms):
    ans = len(rooms)
    for i, ch in enumerate(rooms):
        if ch == '1':
            ans = max(ans, 2 * (len(rooms) - i))
            break
    for i, ch in enumerate(reversed(rooms)):
        if ch == '1':
            ans = max(ans, 2 * (len(rooms) - i))
            break
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        print(solve(input()))
