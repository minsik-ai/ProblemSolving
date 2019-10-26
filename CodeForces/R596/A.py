def solve(d_a, d_b):
    if d_a == d_b:
        return f'{d_a}0 {d_a}1'
    if d_a + 1 == d_b:
        return f'{d_a} {d_b}'
    if d_a == 9 and d_b == 1:
        return f'9 10'
    return '-1'


if __name__ == "__main__":
    a, b = [int(r) for r in input().split(' ')]
    print(solve(a, b))
