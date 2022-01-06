"""
Title : 골목 대장 호석 - 기능성
Link : https://www.acmicpc.net/problem/20168
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M, A, B, C = MIIS()
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = MIIS()
    roads[u].append((v, c))
    roads[v].append((u, c))

visited = [False] * (N + 1)
ans = -1
# maximum cost, total cost, point
heap = [(0, 0, A)]
while heap:
    max_cost, total_cost, p = heapq.heappop(heap)
    if p == B:
        ans = max_cost
        break
    if visited[p]:
        continue
    visited[p] = True
    for q, c in roads[p]:
        if total_cost + c > C:
            continue
        heapq.heappush(heap, (max(max_cost, c), total_cost + c, q))

print(ans)
