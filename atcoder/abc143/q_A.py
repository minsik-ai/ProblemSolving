def solve(a, b):
    ans = a - 2 * b
    if ans < 0:
        return 0

    return ans


if __name__ == "__main__":
    raw = input()
    a, b = raw.split(' ')
    a, b = int(a), int(b)
    print(solve(a, b))
