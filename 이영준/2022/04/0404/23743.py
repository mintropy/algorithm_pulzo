"""
Title : 방탈출
Link : https://www.acmicpc.net/problem/23743
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parent(parents, x):
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(parents, x, y):
    if x > y:
        x, y = y, x
    parents[y] = x
    return parents


if __name__ == "__main__":
    N, M = MIIS()
    routes = [tuple(MIIS()) for _ in range(M)]
    exits = tuple(MIIS())
    routes += [(0, idx + 1, cost) for idx, cost in enumerate(exits)]
    routes.sort(key=lambda x:x[2])
    
    parents = list(range(N + 1))
    dist = 0
    for a, b, c in routes:
        a, b = find_parent(parents, a), find_parent(parents, b)
        if a == b:
            continue
        dist += c
        parents = union_parent(parents, a, b)
    
    print(dist)
