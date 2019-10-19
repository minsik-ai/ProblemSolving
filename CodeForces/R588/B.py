def pr(x):
    print(x, end='')


def solve(n, k, digits):
    if k == 0:
        return print(digits)
    if n == 1:
        return print('0')
    cur_k = k
    for i, d in enumerate(digits):
        if cur_k > 0:
            if i == 0 and d > '1':
                pr('1')
                cur_k -= 1
            elif i > 0 and d > '0':
                pr('0')
                cur_k -= 1
            else:
                pr(d)
        else:
            pr(d)


if __name__ == "__main__":
    read = input()
    n, k = [int(c) for c in read.split(' ')]
    read = input()
    S_raw = read
    solve(n, k, S_raw)
