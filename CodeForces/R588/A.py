
def solve(cand_list):
    tot = sum(cand_list)

    rem = tot % 2
    if rem != 0:
        return "NO"

    div = tot // 2

    # Should be fine without dp because there are only 4
    def calc(idx, cur_sum) -> bool:
        if idx >= len(cand_list):
            return False
        if cur_sum == div:
            return True

        return calc(idx + 1, cur_sum) or calc(idx + 1, cur_sum + cand_list[idx])

    if calc(0, 0):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    read = input()
    candles = [int(r) for r in read.split(' ')]
    print(solve(candles))
