import collections


def solve(inputs, q):
    inputs = [(int(x), int(y), d) for x, y, d in inputs]

    wests = collections.Counter()
    easts = collections.Counter()
    souths = collections.Counter()
    norths = collections.Counter()

    horizontal_keys = set()
    vertical_keys = set()

    W = E = S = N = 0

    for x, y, d in inputs:
        if d == "W":
            horizontal_keys.add(x)
            wests[x] += 1
            W += 1
        elif d == "E":
            horizontal_keys.add(x)
            easts[x] += 1
            E += 1
        elif d == "S":
            vertical_keys.add(y)
            souths[y] += 1
            S += 1
        else:
            vertical_keys.add(y)
            norths[y] += 1
            N += 1

    horizontal_tuples = sorted([(key, wests[key], easts[key]) for key in horizontal_keys], key=lambda item: item[0])
    vertical_tuples = sorted([(key, souths[key], norths[key]) for key in vertical_keys], key=lambda item: item[0])

    best_horizontal_cand = 0
    if len(horizontal_tuples) >= 1:
        k0, w0, e0 = horizontal_tuples[0]
        if k0 == 0:
            prev_vote = W - (w0 + e0)
        else:
            prev_vote = W
        best_vote = prev_vote

        for i, (k, w, e) in enumerate(horizontal_tuples):
            if k == 0:
                continue

            cand = k + 1
            if cand > q:
                continue

            prev_vote = prev_vote - w + e
            if len(horizontal_tuples) - 1 >= i + 1:
                k_n, w_n, e_n = horizontal_tuples[i + 1]
                if k_n == cand:
                    prev_vote = prev_vote - w_n

            if prev_vote > best_vote:
                best_horizontal_cand = cand
                best_vote = prev_vote

    best_vertical_cand = 0
    if len(vertical_tuples) >= 1:
        k0, s0, n0 = vertical_tuples[0]
        if k0 == 0:
            prev_vote = S - (s0 + n0)
        else:
            prev_vote = S
        best_vote = prev_vote

        for i, (k, s, n) in enumerate(vertical_tuples):
            if k == 0:
                continue

            cand = k + 1
            if cand > q:
                continue
                
            prev_vote = prev_vote - s + n
            if len(vertical_tuples) - 1 >= i + 1:
                k_n, s_n, n_n = vertical_tuples[i + 1]
                if k_n == cand:
                    prev_vote = prev_vote - s_n

            if prev_vote > best_vote:
                best_vertical_cand = cand
                best_vote = prev_vote

    return best_horizontal_cand, best_vertical_cand


t = int(input())
for i in range(1, t + 1):
    p, q = [int(s) for s in input().split(" ")]

    inputs = []
    for j in range(p):
        inputs.append(input().split(" "))

    x, y = solve(inputs, q)

    print("Case #{}: {} {}".format(i, x, y))
