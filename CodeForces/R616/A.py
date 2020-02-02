def solve(n, s):
    # ebne : number is not even but sum of all digits is even.
    # first, delete all digits that are even from the lowest digit until we find an odd number.
    # Then calculate the sum of all digits. If it is odd, remove one odd number.
    digs = []
    # first
    is_odd = False
    while s > 0:
        dig = s % 10
        s //= 10
        if dig % 2 == 0 and not is_odd:
            continue
        is_odd = True
        digs.append(dig)

    # second
    dig_sum = sum(digs)
    if dig_sum == 0:
        return -1
    if dig_sum % 2 == 0:
        return ''.join([str(dig) for dig in reversed(digs)])

    # Odd
    skipped = False
    new_digs = []
    odd_count = 0
    for i, dig in enumerate(digs):
        if dig % 2 == 1 and not skipped and i > 0:
            # Only Skip one
            # First one shouldn't be skipped because it should remain odd.
            skipped = True
            continue
        if dig % 2 == 1:
            odd_count += 1
        new_digs.append(dig)

    if skipped:
        return ''.join([str(dig) for dig in reversed(new_digs)])

    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = int(input())
        print(solve(n, s))
