def solve(lines):
    lines.sort()
    div = len(lines) // 2
    sum_x = sum(lines[:div])
    sum_y = sum(lines[div:])
    return sum_x ** 2 + sum_y ** 2


if __name__ == "__main__":
    n = int(input())
    lines = [int(r) for r in input().split(' ')]
    print(solve(lines))
