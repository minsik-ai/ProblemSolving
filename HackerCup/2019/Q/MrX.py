DEBUG = False


def parsed(inputs):
    outputs = []
    ops = []

    for ch in inputs:
        if ch == '(':
            pass
        elif ch == '1' or ch == '0':
            outputs.append(int(ch))
        elif ch == '|' or ch == '&' or ch == '^':
            ops.append(ch)
        elif ch == ')':
            o1 = outputs.pop()
            o2 = outputs.pop()
            op = ops.pop()
            if op == '|':
                if o1 == 1 or o2 == 1:
                    outputs.append(1)
                else:
                    outputs.append(0)
            elif op == '&':
                if o1 == 1 and o2 == 1:
                    outputs.append(1)
                else:
                    outputs.append(0)
            elif op == '^':
                if o1 != o2:
                    outputs.append(1)
                else:
                    outputs.append(0)
    return outputs[0]


def solve(inputs):
    x0line = inputs.replace('x', '0').replace('X', '1')
    x1line = inputs.replace('x', '1').replace('X', '0')

    if parsed(x0line) != parsed(x1line):
        return 1
    else:
        return 0


if DEBUG:
    with open('mr_x.txt', 'r') as f:
        lines = f.read().splitlines()
        import collections

        lines = collections.deque(lines)
        input_f = lines.popleft
else:
    input_f = input

t = int(input_f())
for i in range(1, t + 1):
    line = input_f()

    res = solve(line)

    print("Case #{}: {}".format(i, res))
