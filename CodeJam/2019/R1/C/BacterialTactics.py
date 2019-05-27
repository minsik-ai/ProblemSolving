import copy
from operator import itemgetter

import numpy as np


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

        partial_row_filled_states = [fill_partial_rows(new_inputs, i) for i in range(r)]
        partial_col_filled_states = [fill_partial_cols(new_inputs, i) for i in range(c)]

        all_possible_states_winning_result = []
        for matrix in set(partial_row_filled_states + partial_col_filled_states):
            if matrix in memoized:
                all_possible_states_winning_result.append(memoized[matrix])
                continue
            result = check_is_winning(matrix)
            memoized[matrix] = result
            all_possible_states_winning_result.append(result)

        return any(all_possible_states_winning_result)

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


def fill_partial_rows(inputs, i):
    new_row = inputs[i]
    tuple_new_row = list(enumerate(new_row))

    list_of_tuples = []
    cur_tuples = []
    for tuple in tuple_new_row:
        if tuple[1] == 'x':
            if cur_tuples:
                list_of_tuples.append(cur_tuples)
                cur_tuples = []
            continue
        cur_tuples.append(tuple)

    if cur_tuples:
        list_of_tuples.append(cur_tuples)

    partial_rows = [tuples for tuples in list_of_tuples if '#' not in map(itemgetter(1), tuples)]

    new_input_list = []
    for partial_row in partial_rows:
        new_inputs = copy.deepcopy(inputs)
        for index, item in partial_row:
            new_inputs[i][index] = 'x'
        new_input_list.append(new_inputs)

    return new_input_list


def fill_partial_cols(inputs, i):
    new_col = inputs[:, i]
    tuple_new_col = list(enumerate(new_col))

    list_of_tuples = []
    cur_tuples = []
    for tuple in tuple_new_col:
        if tuple[1] == 'x':
            if cur_tuples:
                list_of_tuples.append(cur_tuples)
                cur_tuples = []
            continue
        cur_tuples.append(tuple)

    if cur_tuples:
        list_of_tuples.append(cur_tuples)

    partial_cols = [tuples for tuples in list_of_tuples if '#' not in map(itemgetter(1), tuples)]

    new_input_list = []
    for partial_col in partial_cols:
        new_inputs = copy.deepcopy(inputs)
        for index, item in partial_col:
            new_inputs[index][i] = 'x'
        new_input_list.append(new_inputs)

    return new_input_list


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
