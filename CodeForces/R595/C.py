def solve(q):
    rep = []
    while q:
        rem = q % 3
        rep.append(rem)
        q //= 3
    rep.append(0)
    i = 0
    # print(rep)
    while i < len(rep):
        if rep[i] == 2:
            rep[i] = 0
            for j in range(i + 1, len(rep)):
                if rep[j] == 0:
                    rep[j] = 1
                    for k in range(j):
                        rep[k] = 0
                    i = j
                    break
        i += 1
    # print(rep)
    ans = 0
    for i, num in enumerate(rep):
        ans += num * (3 ** i)
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
