def solve(n, p):
    cur, count = n, 0
    while True:
        count += 1
        cur -= p
        if cur <= 0:
            break
        binary = format(cur, 'b')
        min_count, max_count = 0, 0
        for i, ch in enumerate(reversed(binary)):
            if ch == '1':
                min_count += 1
                max_count += 2 ** i
        if max_count >= count >= min_count:
            return count

    return -1


if __name__ == "__main__":
    n, p = [int(r) for r in input().split(' ')]
    print(solve(n, p))
