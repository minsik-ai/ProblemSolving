import collections
import math

len_s = collections.defaultdict(dict)


def min_len(x_1, y_1, x_2, y_2):
    l_1 = len_s[(x_1, y_1)].get((x_2, y_2))
    if l_1 is not None:
        return l_1
    l_2 = len_s[(x_2, y_2)].get((x_1, y_1))
    if l_2 is not None:
        return l_2
    if x_1 == x_2 and y_1 == y_2:
        len_s[(x_1, y_1)][(x_2, y_2)] = 0
        return 0

    len_s[(x_1, y_1)][(x_2, y_2)] = math.inf
    for coord in [(x_1 - 1, y_1), (x_1 + 1, y_1), (x_1, y_1 - 1), (x_1, y_1 + 1)]:
        x, y = coord
        if x < 0 or x >= h or y < 0 or y >= w:
            continue
        val = mat[x][y]
        if val == '#':
            continue
        len_s[(x_1, y_1)][(x_2, y_2)] = min(len_s[(x_1, y_1)][(x_2, y_2)], min_len(x, y, x_2, y_2) + 1)
    return len_s[(x_1, y_1)][(x_2, y_2)]


def solve(h, w, mat):
    ans = 0
    for x_1, row1 in enumerate(mat):
        for y_1, val1 in enumerate(row1):
            if val1 == '#':
                continue
            for x_2, row2 in enumerate(mat):
                for y_2, val2 in enumerate(row2):
                    if val2 == '#':
                        continue
                    l = min_len(x_1, y_1, x_2, y_2)
                    print(f'{x_1}, {y_1}, {x_2}, {y_2} : {l}')
                    if l == math.inf:
                        continue
                    ans = max(ans, l)
    return ans


def input_to_int():
    return [int(r) for r in input().split(' ')]


if __name__ == "__main__":
    h, w = input_to_int()
    mat = []
    for _ in range(h):
        mat.append(list(input()))
    print(solve(h, w, mat))
