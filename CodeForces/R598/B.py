def solve(elems):
    i = 0
    j = len(elems)
    while i < len(elems) - 1:
        min_index = i
        for k in range(i, j):
            if elems[min_index] > elems[k]:
                min_index = k
        for m in range(min_index - 1, i - 1, -1):
            elems[m], elems[m + 1] = elems[m + 1], elems[m]
        if min_index == i:
            i += 1
            continue
        i = min_index
    return ' '.join([str(e) for e in elems])


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        elems = [int(r) for r in input().split(' ')]
        print(solve(elems))
