DEBUG = False


def solve(n, m, conds):
    return


if DEBUG:
    with open('graphsasaservice.txt', 'r') as f:
        lines = f.read().splitlines()
        import collections

        lines = collections.deque(lines)
        in_f = lines.popleft
else:
    in_f = input

t = int(in_f())
for i in range(1, t + 1):
    n_m = in_f().split()

    n = int(n_m[0])
    m = int(n_m[1])

    conds = []
    for j in range(m):
        x_y_z = in_f().split()
        conds.append((x_y_z[0], x_y_z[1], x_y_z[2]))

    res = solve(n, m, conds)

    print("Case #{}: {}".format(i, res))
