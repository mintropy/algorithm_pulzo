"""
title : 최소비용 구하기
Link : https://www.acmicpc.net/problem/1916
"""


from sys import stdin
from heapq import *

INF = int(1e10)
# 도시 개수
n = int(stdin.readline().strip())
# 버스 개수
m = int(stdin.readline().strip())
# 버스 망, 각 인덱스에서 출발하는 버스, 비용
city = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    city[a].append((b, c))
# 출발, 도착 도시
start, end = map(int, stdin.readline().split())
results = [INF for _ in range(n + 1)]

def dijkstra(start, end):
    global results, city
    results[start] = 0
    heap = []
    # 비용, 도시
    heappush(heap, (0, start))
    while heap:
        cost, x = heappop(heap)
        if x == end:
            return cost
        for y, c in city[x]:
            if cost + c >= results[y]:
                continue
            heappush(heap, (cost + c, y))
            results[y] = cost + c


print(dijkstra(start, end))