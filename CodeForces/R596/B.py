import collections


def solve(n, k, d, a_s):
    # d consecutive segment, with minimum different elements
    elems = collections.Counter(a_s[0:d])
    cur = len(elems)
    ans = cur
    i, j = 0, d - 1
    while True:
        prev_i = a_s[i]
        i += 1
        j += 1
        if j >= len(a_s):
            break
        next_j = a_s[j]

        elems[prev_i] -= 1
        if elems[prev_i] == 0:
            cur -= 1
        elems[next_j] += 1
        if elems[next_j] == 1:
            cur += 1
        ans = min(ans, cur)
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, d = [int(r) for r in input().split(' ')]
        a_s = [int(r) for r in input().split(' ')]
        print(solve(n, k, d, a_s))
