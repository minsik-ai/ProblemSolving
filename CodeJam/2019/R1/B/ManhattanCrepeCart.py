def solve(inputs, q):
    inputs = [(int(x), int(y), d) for x, y, d in inputs]

    horizontal_cands = [x + 1 for x, y, d in inputs]
    horizontal_cands.append(0)

    vertical_cands = [y + 1 for x, y, d in inputs]
    vertical_cands.append(0)

    max_horizontal = 0
    max_count = 0
    for cand in horizontal_cands:
        count = 0
        for x, y, d in inputs:
            if d == "E" and x < cand:
                count += 1
            elif d == "W" and x > cand:
                count += 1
        if count > max_count:
            max_count = count
            max_horizontal = cand
        elif count == max_count and cand < max_horizontal:
            max_horizontal = cand

    max_vertical = 0
    max_count = 0
    for cand in vertical_cands:
        count = 0
        for x, y, d in inputs:
            if d == "N" and y < cand:
                count += 1
            elif d == "S" and y > cand:
                count += 1
        if count > max_count:
            max_count = count
            max_vertical = cand
        elif count == max_count and cand < max_vertical:
            max_vertical = cand

    return max_horizontal, max_vertical


t = int(input())
for i in range(1, t + 1):
    p, q = [int(s) for s in input().split(" ")]

    inputs = []
    for j in range(p):
        inputs.append(input().split(" "))

    x, y = solve(inputs, q)

    print("Case #{}: {} {}".format(i, x, y))
