"""
Title : 중량제한
Link : https://www.acmicpc.net/problem/1939
"""

import heapq
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    bridges = [{} for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = MIIS()
        if b not in bridges[a] or c > bridges[a][b]:
            bridges[a][b] = c
        if a not in bridges[b] or c > bridges[b][a]:
            bridges[b][a] = c

    st, end = MIIS()
    maximum_weights = [0] * (N + 1)
    heap = [(-1_000_000_000, st)]
    while heap:
        weight, pos = heapq.heappop(heap)
        if maximum_weights[pos]:
            continue
        maximum_weights[pos] = -weight
        for next_pos, limit in bridges[pos].items():
            next_weight = min(-weight, limit)
            if maximum_weights[next_pos]:
                continue
            heapq.heappush(heap, (-next_weight, next_pos))
    print(maximum_weights[end])
