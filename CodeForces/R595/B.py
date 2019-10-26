def solve(n, p_s):
    sets = []
    visited = set([])
    for i, p in enumerate(p_s):
        if i in visited:
            continue
        new_indices = set([])
        cur = i
        while True:
            if cur in new_indices:
                break
            new_indices.add(cur)
            visited.add(cur)
            cur = p_s[cur] - 1
        sets.append(new_indices)
    ans = [0 for _ in range(n)]
    for indices in sets:
        for index in indices:
            ans[index] = str(len(indices))
    return ' '.join(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        p_s = [int(r) for r in input().split(' ')]
        print(solve(n, p_s))
