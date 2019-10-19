def solve(n, p, w, d):
    # try to start with maximum number of wins
    # if mod != 0, continue checking reminder

    # Tot count only going up
    win_count = p // w
    draw_count = (p % w) // d
    while win_count >= 0:
        rem_p = p - w * win_count
        draw_count = rem_p // d
        if win_count + draw_count > n:
            # Too many
            return -1

        if rem_p % d == 0:
            # Total
            break

        win_count -= 1

    loss_count = n - (win_count + draw_count)
    return win_count, draw_count, loss_count


if __name__ == "__main__":
    n, p, w, d = [int(e) for e in input().split(' ')]
    ans = solve(n, p, w, d)
    if ans == -1:
        print(-1)
    else:
        x, y, z = ans
        print(f'{x} {y} {z}')
