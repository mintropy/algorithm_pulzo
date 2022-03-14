"""
Title : 운동
Link : https://www.acmicpc.net/problem/1956
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

V, E = MIIS()
INF = int(10e9)

# roads = [[] for _ in range(V + 1)]
roads = {i:[] for i in range(1, V + 1)}
for _ in range(E):
    a, b, c = MIIS()
    roads[a].append((b, c))

ans = INF
for st in range(1, V + 1):
    distance = [INF] * (V + 1)
    heap = []
    for next_city, next_dist in roads[st]:
        distance[next_city] = next_dist
        heap.append((next_dist, next_city))
    heapq.heapify(heap)
    
    result = INF
    while heap:
        now_dist, now_city = heapq.heappop(heap)
        if now_city == st:
            result = now_dist
            break
        if distance[now_city] < now_dist:
            continue
        for next_city, next_dist in roads[now_city]:
            if distance[next_city] > now_dist + next_dist:
                distance[next_city] = now_dist + next_dist
                heapq.heappush(heap, (now_dist + next_dist, next_city))
    
    if ans > result:
        ans = result

print(ans if ans != INF else -1)


'''
# Floyd-Warshall
V, E = MIIS()
INF = 10e9

roads = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = MIIS()
    roads[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        if k == i or roads[i][k] == INF:
            continue
        for j in range(1, V + 1):
            if k == j or roads[k][j] == INF:
                continue
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]

ans = min(roads[i][i] for i in range(1, V  + 1))
print(ans if ans != INF else -1)
'''
