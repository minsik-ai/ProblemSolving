import collections
import heapq


def solve(cards):
    counter = collections.Counter(cards)

    counts = [(-count, card) for card, count in counter.items()]
    # Max heap
    heapq.heapify(counts)

    ans = [0] * len(cards)
    for k in range(1, len(cards) + 1):
        times = 0
        heap = counts.copy()
        while heap:
            if len(heap) < k:
                break
            to_remove = [heapq.heappop(heap) for _ in range(k)]
            for e in to_remove:
                count, card = e
                count = - count - 1
                if count == 0:
                    continue
                heapq.heappush(heap, (-count, card))
            times += 1
        ans[k - 1] = times

    return ans


if __name__ == "__main__":
    n = int(input())
    a_s = [int(l) for l in input().split(' ')]
    for ans in solve(a_s):
        print(ans)
