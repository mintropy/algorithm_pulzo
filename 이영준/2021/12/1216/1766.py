"""
Title : 문제집
Link : https://www.acmicpc.net/problem/1766
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N, M = MIIS()
pre_series = [0 for _ in range(N + 1)]
post_series = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = MIIS()
    pre_series[b] += 1
    post_series[a].append(b)

heap = []
for i in range(1, N + 1):
    if pre_series[i] == 0:
        heap.append(i)
heapq.heapify(heap)

topological_order = []
while heap:
    i = heapq.heappop(heap)
    topological_order.append(i)
    for j in post_series[i]:
        pre_series[j] -= 1
        if pre_series[j] == 0:
            heapq.heappush(heap, j)

print(*topological_order)
