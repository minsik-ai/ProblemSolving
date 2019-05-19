def solve(inputs, a):
    # Answer must win against every match-up.
    orig_input_length = len(inputs)

    ans = []

    total_wins = 0

    choices = ['R', 'P', 'S']
    for i in range(0, 500):
        choice_wins = [0, 0, 0]
        choice_win_inputs = [[], [], []]
        for j, choice in enumerate(choices):
            # find max choice
            for k, input in enumerate(inputs):
                n_char = input[i % len(input)]
                res = win_lose(choice, n_char)
                if res == -1:
                    choice_wins[j] = -1
                    break
                if res == 1:
                    choice_wins[j] += 1
                    choice_win_inputs[j].append(k)

        wins = max(choice_wins)

        if wins < 0:
            return 'IMPOSSIBLE'

        choice_index = choice_wins.index(wins)
        win_choice = choices[choice_index]

        inputs = [item for j, item in enumerate(inputs) if j not in choice_win_inputs[choice_index]]

        ans.append(win_choice)
        total_wins += wins

        if total_wins == orig_input_length:
            return ''.join(ans)

    return 'IMPOSSIBLE'


def win_lose(choice, n_char):
    if (choice == 'R' and n_char == 'S') or (choice == 'P' and n_char == 'R') or (choice == 'S' and n_char == 'P'):
        return 1  # Win
    if choice == n_char:
        return 0  # Draw

    # Lose
    return -1


t = int(input())
for i in range(1, t + 1):
    a = int(input())

    inputs = []
    for j in range(a):
        inputs.append(list(input()))

    ans = solve(inputs, a)

    print("Case #{}: {}".format(i, ans))
