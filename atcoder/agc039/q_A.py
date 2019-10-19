def solve(text, count):
    if len(text) == 1:
        return count // 2

    # split chars into first part & last part & middle parts & joint parts
    first_ch = text[0]

    # Endpoints exclusive
    first_index = -1
    middle_index = -1

    for i, ch in enumerate(text):
        if ch == first_ch:
            continue
        else:
            first_index = i
            break

    if first_index == -1:
        # All Same Character
        return (len(text) * count) // 2

    for i in range(len(text) - 1, first_index - 1, -1):
        if text[i] == first_ch:
            continue
        else:
            middle_index = i + 1
            break

    first_part = text[:first_index]
    middle_part = text[first_index:middle_index]
    end_part = text[middle_index:]
    joint_part = end_part + first_part

    def calc_changes(raw_part):
        change = 0

        part = [ch for ch in raw_part]

        for i, ch in enumerate(part):
            if i == 0:
                continue
            if part[i - 1] == part[i] and part[i - 1] != '!':
                part[i] = '!'  # Any char fine since we can choose any
                change += 1
                continue

        return change

    return calc_changes(first_part) + calc_changes(middle_part) * count + \
           calc_changes(joint_part) * (count - 1) + calc_changes(end_part)


if __name__ == "__main__":
    s = input()
    k = int(input())
    print(solve(s, k))
