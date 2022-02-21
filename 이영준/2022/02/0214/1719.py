"""
title : 택배
Link : https://www.acmicpc.net/problem/1719
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def search(dist: list, routes: list, N: int, st: int) -> list:
    heap = [(t, x, x) for x, t in routes[st]]
    visited = [1_000_000_000] * (N + 1)
    visited[st] = 0
    for x, t in routes[st]:
        visited[x] = t
    while heap:
        cost, pos, first = heapq.heappop(heap)
        if visited[pos] < cost:
            continue
        dist[st - 1][pos - 1] = first
        for _pos, _cost in routes[pos]:
            if cost + _cost < visited[_pos]:
                heap.append((cost + _cost, _pos, first))
                visited[_pos] = cost + _cost
        heapq.heapify(heap)
    return dist


def solution() -> None:
    N, M = MIIS()
    routes = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, t = MIIS()
        routes[x].append((y, t))
        routes[y].append((x, t))

    dist = [[0] * N for _ in range(N)]
    for i in range(1, N + 1):
        dist = search(dist, routes, N, i)

    for i in range(N):
        for j in range(N):
            if i == j:
                print('-', end=' ')
            else:
                print(dist[i][j], end=' ')
        print()


solution()
