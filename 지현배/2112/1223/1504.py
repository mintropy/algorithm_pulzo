import sys
from heapq import *
input = sys.stdin.readline
N, E = map(int, input().split())
edges = [[] for _ in range(N + 1)]
MAX = 800000

def dijk(n1, n2):
    dist = [MAX] * (N + 1)
    dist[n1] = 0
    heap = [(0, n1)]
    while heap:
        cost, node = heappop(heap)
        if cost > dist[node]:
            continue
        for next, weight in edges[node]:
            if dist[next] > cost + weight:
                dist[next] = cost + weight
                heappush(heap, (dist[next], next))
    return dist[1], dist[N], dist[n2]

def sol():
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))
    v1, v2 = map(int, input().split())

    # v1 -> 1 / N / v2
    v1_1, v1_N, v1_v2 = dijk(v1, v2)
    if v1_v2 == MAX or v1_1 == MAX and v1_N == MAX:
        return -1
    # v2 -> 1 / N
    v2_1, v2_N, _ = dijk(v2, v1)
    if v2_1 == MAX and v2_N == MAX:
        return -1
    v1_first = -1
    v2_first = -1
    if v1_1 != MAX and v2_N != MAX:
        v1_first = v1_1 + v2_N + v1_v2
    if v1_N != MAX and v2_1 != MAX:
        v2_first = v1_N + v2_1 + v1_v2

    if v1_first != -1 and v2_first != -1:
        return min(v1_first, v2_first)
    if v1_first != -1 and v2_first == -1:
        return v1_first
    if v1_first == -1 and v2_first != -1:
        return v2_first
    return -1

print(sol())
