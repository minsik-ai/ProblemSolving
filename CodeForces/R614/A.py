def solve(n, s, a_k):
    # O(n) solution
    for i in range(0, n):
        c_l = s - i
        if c_l < 1:
            c_l = 1
        c_h = s + i
        if c_h > n:
            c_h = n
        if c_l not in a_k or c_h not in a_k:
            return i
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s, k = [int(r) for r in input().split(' ')]
        a_k = {int(r) for r in input().split(' ')}
        print(solve(n, s, a_k))
