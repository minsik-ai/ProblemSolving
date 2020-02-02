def solve(n, m, k, a_s):
    ans = 1
    # if k >= m, rest of k is meaningless. Thus reset k here.
    k = min(k, m - 1)

    rand_thresh = m - 1 - k

    for st_init in range(k + 1):
        # Handle fixed case
        ed_init = n - 1 - (k - st_init)
        rands = max(rand_thresh, 0)

        st = st_init
        ed = ed_init
        if rands > 0:
            rand_ans = 10 ** 9
            for st_offset in range(rands + 1):
                ed_offset = rands - st_offset
                rand_ans = min(rand_ans, max(a_s[st + st_offset], a_s[ed - ed_offset]))
            ans = max(ans, rand_ans)
        else:
            ans = max(ans, max(a_s[st], a_s[ed]))

    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = [int(ch) for ch in input().split(' ')]
        a_s = [int(ch) for ch in input().split(' ')]
        print(solve(n, m, k, a_s))
