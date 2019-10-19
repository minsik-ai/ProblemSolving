DEBUG = False


def solve(n, k, string):
    chars = list(string)

    # 1st case
    b_starts = []
    i = 0
    while i < n:
        if (i == 0 or chars[i - 1] == 'A') and chars[i] == 'B':
            b_starts.append(i)
        i += 1

    # 2nd case
    merges = {}
    for i in b_starts:
        start_i = i
        diff_count = 0
        while i < n:
            ch = chars[i]
            if ch == 'B':
                diff_count += 1
            elif ch == 'A':
                if chars[i - 1] == 'B':
                    merges[(start_i, i)] = diff_count
                diff_count -= 1
            i += 1

    for key in merges:
        diff = merges[key]
        if diff <= k:
            continue
        start, end = key


    return


if DEBUG:
    with open('graphsasaservice.txt', 'r') as f:
        lines = f.read().splitlines()
        import collections

        lines = collections.deque(lines)
        in_f = lines.popleft
else:
    in_f = input

t = int(in_f())
for i in range(1, t + 1):
    n_k = in_f().split()

    n = int(n_k[0])
    k = int(n_k[1])

    string = in_f()

    res = solve(n, k, string)

    print("Case #{}: {}".format(i, res))
