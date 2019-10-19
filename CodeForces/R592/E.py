import heapq
import collections


def solve(n, k, a_list):
    min_heap = a_list.copy()
    max_heap = [-1 * e for e in a_list.copy()]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    counter = collections.Counter(a_list)
    for i in range(k):
        min_e = min_heap[0]
        max_e = -max_heap[0]
        if max_e == min_e:
            return 0
        if max_e > min_e:
            # max_e is more likely to get smaller
            if counter[max_e] < counter[min_e]:
                counter[max_e] -= 1
                max_e -= 1
                heapq.heapreplace(max_heap, -max_e)
                counter[max_e] += 1
            else:
                counter[min_e] -= 1
                min_e += 1
                heapq.heapreplace(min_heap, min_e)
                counter[min_e] += 1

    return - max_heap[0] - min_heap[0]


if __name__ == "__main__":
    n, k = [int(e) for e in input().split(' ')]
    a_list = [int(e) for e in input().split(' ')]
    print(solve(n, k, a_list))
