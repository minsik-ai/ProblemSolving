import collections

def primes_sieve2(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


def solve(n, k, a_s):
    prime_elems = collections.defaultdict(list)
    for p in primes_sieve2(max(a_s)):
        prime_elems[p] =

    return ans


if __name__ == "__main__":
    n, k = [int(r) for r in input().split(' ')]
    a_s = [int(r) for r in input().split(' ')]
    print(solve(n, k, a_s))
