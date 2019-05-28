import copy
from operator import itemgetter

import numpy as np


def hash(matrix, r, c):
    partial_strings = []
    print(matrix)
    for i in range(len(matrix)):
        char_list = matrix[i].tolist()
        print(char_list)
        partial_strings.append(''.join(char_list))

    return ''.join(partial_strings)


def solve(inputs, r, c):
    # Get possible first moves
    # Recursively check for possible moves afterward that they are winning moves.
    # Memoize as needed.

    possible_rows = []
    for i in range(r):
        if '#' in inputs[i]:
            continue
        else:
            possible_rows.append(i)

    possible_cols = []
    for i in range(c):
        if '#' in inputs[:, i]:
            continue
        else:
            possible_cols.append(i)

    win_counter = 0

    memoized = {}

    def check_is_winning(new_inputs):

        if '.' not in new_inputs:
            return False

        print(r)

        partial_row_filled_states = [fill_partial_rows(new_inputs, m) for m in range(r)]
        partial_col_filled_states = [fill_partial_cols(new_inputs, n) for n in range(c)]

        partial_row_filled_states = list(filter(lambda x: x, partial_row_filled_states))
        partial_col_filled_states = list(filter(lambda x: x, partial_col_filled_states))

        print('r : {}, row : {}'.format(r, partial_row_filled_states))
        print('c : {}, col : {}'.format(c, partial_col_filled_states))

        winning_results = []
        for matrix in partial_row_filled_states + partial_col_filled_states:
            hashKey = hash(matrix, r, c)
            if hashKey in memoized:
                winning_results.append(memoized[hashKey])
                continue
            result = check_is_winning(matrix)
            memoized[hashKey] = result
            winning_results.append(result)

        return any(winning_results)

    for i in possible_rows:
        new_inputs = copy.deepcopy(inputs)

        fill_row(new_inputs, i)
        if check_is_winning(new_inputs):
            win_counter += c

    for i in possible_cols:
        new_inputs = copy.deepcopy(inputs)

        fill_col(new_inputs, i)
        if check_is_winning(new_inputs):
            win_counter += r

    return win_counter


def fill_partial(line, is_row):
    tuple_new_line = list(enumerate(line))
    print('{} : {}'.format(i, tuple_new_line))

    list_of_tuples = []
    cur_tuples = []
    for tuple in tuple_new_line:
        if tuple[1] == 'x':
            if cur_tuples:
                list_of_tuples.append(cur_tuples)
                cur_tuples = []
            continue
        cur_tuples.append(tuple)

    if cur_tuples:
        list_of_tuples.append(cur_tuples)

    print('{} : {}'.format(i, list_of_tuples))

    partial_lines = [tuples for tuples in list_of_tuples if '#' not in map(lambda x: x[1], tuples)]

    print(partial_lines)

    new_input_list = []
    for partial_line in partial_lines:
        new_inputs = copy.deepcopy(inputs)
        for index, item in partial_line:
            if is_row:
                new_inputs[i][index] = 'x'
            else:
                new_inputs[index][i] = 'x'
        print('Input : {}'.format(new_inputs))
        new_input_list.append(new_inputs)

    print('Input List : {}'.format(new_input_list))

    return new_input_list


def fill_partial_rows(inputs, i):
    new_row = inputs[i]
    return fill_partial(new_row, True)


def fill_partial_cols(inputs, i):
    new_col = inputs[:, i]
    return fill_partial(new_col, False)


def fill_row(inputs, i, j=0, k=None):
    if k is None:
        k = len(inputs[i])
    inputs[i, j:k] = ['x'] * (k - j)


def fill_col(inputs, i, j=0, k=None):
    if k is None:
        k = len(inputs[:, i])
    inputs[j: k, i] = ['x'] * (k - j)


t = int(input())
for i in range(1, t + 1):
    r_c = list(map(lambda x: int(x), input().split()))
    r = r_c[0]
    c = r_c[1]

    inputs = []
    for j in range(r):
        inputs.append(list(input()))

    inputs = np.array(inputs)

    ans = solve(inputs, r, c)

    print("Case #{}: {}".format(i, ans))
