def solve(n, a_s):
    left = [True] * n
    right = [True] * n
    # Strict relationship invariant
    for i, a in enumerate(a_s):
        if a < i:
            left[i] = False
        if a < n - 1 - i:
            right[i] = False

    l_max = n - 1
    for i, l in enumerate(left):
        if not l:
            l_max = i - 1
            break

    r_max = n - 1
    for i, r in enumerate(reversed(right)):
        if not r:
            r_max = i - 1
            break

    if l_max + r_max + 2 < n:
        return "No"
    if l_max != r_max:
        return "Yes"

    # l_max == r_max
    # Even elements & same max number at middle
    if l_max + r_max + 2 == n and l_max == r_max and a_s[l_max] == a_s[n - 1 - r_max]:
        return "No"

    return "Yes"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_s = [int(ch) for ch in input().split(' ')]
        print(solve(n, a_s))
