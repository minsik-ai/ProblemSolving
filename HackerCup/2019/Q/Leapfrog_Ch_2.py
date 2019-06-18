DEBUG = False


def solve(line):
    n = len(line)
    b_s = line.count('B')

    if n == 2:
        return False

    if n == 3 and b_s == 1:
        return True

    rem_s = n - 1

    return (b_s + 1 <= rem_s) and (2 <= b_s)


if DEBUG:
    with open('leapfrog_ch_.txt', 'r') as f:
        lines = f.read().splitlines()
        import collections

        lines = collections.deque(lines)
        in_f = lines.popleft
else:
    in_f = input

t = int(in_f())
for i in range(1, t + 1):
    line = in_f()

    res = solve(line)
    if res:
        res = 'Y'
    else:
        res = 'N'

    print("Case #{}: {}".format(i, res))