import sys
from heapq import *
input = sys.stdin.readline
V, E = map(int, input().split())
MAX = V * 10 + 1
K = int(input())
# 인접리스트
routes = [[] for _ in range(V + 1)]
# 거리 dp
dist = [MAX for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    routes[u].append((v, w))
queue = [(0, K)]
dist[K] = 0
# 다익스트라
while queue:
    d, node = heappop(queue)
    if dist[node] < d: continue
    for v, w in routes[node]:
        if dist[v] > d + w:
            dist[v] = d + w
            heappush(queue, (d + w, v))
# 결과
for i in range(1, V + 1):
    if dist[i] == MAX:
        print('INF')
    else:
        print(dist[i])