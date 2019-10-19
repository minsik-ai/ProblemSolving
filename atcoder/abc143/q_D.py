def solve(lengths):
    # O(n**2) solution?
    # if we have a, b , with a > b
    # then a < c + b, c < a + b -> a - b < c < a + b is the only condition
    # let's say we iterate from max b and max a , so there will be no duplicates.
    # the diff b - a is the only important thing, since a + b will always be bigger than c
    # So we could do DP on this.

    c_counts = {}
    lengths.sort(reverse=True)
    ans = 0
    for i in range(len(lengths)):
        for j in range(i + 1, len(lengths)):
            a, b = lengths[i], lengths[j]
            c_limit = (j, a - b)
            if c_limit in c_counts:
                ans += c_counts[c_limit]
                continue
            c_count = 0
            for k in range(j + 1, len(lengths)):
                c = lengths[k]
                if c > a - b:
                    c_count += 1
                else:
                    # Descending so..
                    break
            c_counts[c_limit] = c_count
            ans += c_count
    return ans


if __name__ == "__main__":
    n = int(input())
    l_s = [int(l) for l in input().split(' ')]
    print(solve(l_s))
