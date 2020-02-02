import collections


def solve(n, m, hist):
    cor = 0
    pen = 0
    for p, tries in hist.items():
        for i, t in enumerate(tries):
            if t == 'AC':
                cor += 1
                pen += i
                break
    return '{0} {1}'.format(cor, pen)


def input_to_int():
    return [int(r) for r in input().split(' ')]


if __name__ == "__main__":
    n, m = input_to_int()
    hist = collections.defaultdict(list)
    for _ in range(m):
        p, s = input().split(' ')
        hist[p].append(s)
    print(solve(n, m, hist))
