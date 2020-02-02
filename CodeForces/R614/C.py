lane1 = set()
lane2 = set()
lines_lane1 = set()
lines_lane2 = set()


def solve(cell):
    r, c = cell
    if r == 1:
        if c in lane1:
            lane1.remove(c)
            if c in lines_lane1:
                lines_lane1.remove(c)
                if c - 1 in lines_lane2:
                    corr = [c - 2, c - 1]
                    if not any([e in lines_lane1 for e in corr]):
                        lines_lane2.remove(c - 1)
                if c in lines_lane2:
                    corr = [c - 1, c + 1]
                    if not any([e in lines_lane1 for e in corr]):
                        lines_lane2.remove(c)
                if c + 1 in lines_lane2:
                    corr = [c + 1, c + 2]
                    if not any([e in lines_lane1 for e in corr]):
                        lines_lane2.remove(c + 1)
        else:
            lane1.add(c)
            added = False
            if c - 1 in lane2:
                added = True
                lines_lane2.add(c - 1)
            if c in lane2:
                added = True
                lines_lane2.add(c)
            if c + 1 in lane2:
                added = True
                lines_lane2.add(c + 1)
            if added:
                lines_lane1.add(c)
    if r == 2:
        if c in lane2:
            lane2.remove(c)
            if c in lines_lane2:
                lines_lane2.remove(c)

                if c - 1 in lines_lane1:
                    corr = [c - 2, c - 1]
                    if not any([e in lines_lane2 for e in corr]):
                        lines_lane1.remove(c - 1)
                if c in lines_lane1:
                    corr = [c - 1, c + 1]
                    if not any([e in lines_lane2 for e in corr]):
                        lines_lane1.remove(c)
                if c + 1 in lines_lane1:
                    corr = [c + 1, c + 2]
                    if not any([e in lines_lane2 for e in corr]):
                        lines_lane1.remove(c + 1)
        else:
            lane2.add(c)
            added = False
            if c - 1 in lane1:
                added = True
                lines_lane1.add(c - 1)
            if c in lane1:
                added = True
                lines_lane1.add(c)
            if c + 1 in lane1:
                added = True
                lines_lane1.add(c + 1)
            if added:
                lines_lane2.add(c)
    if lines_lane1:
        return "No"
    return "Yes"


if __name__ == "__main__":
    n, q = [int(r) for r in input().split(' ')]
    for _ in range(q):
        cell = [int(r) for r in input().split(' ')]
        print(solve(cell))
