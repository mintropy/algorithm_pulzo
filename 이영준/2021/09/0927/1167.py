"""
Title : 트리의 지름
Link : https://www.acmicpc.net/problem/1167
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bfs(p: int) -> tuple:
    q, r = p, 0
    queue = collections.deque([(p, 0)])
    visited = [False] * (v + 1)
    visited[p] = True
    while queue:
        x, d1 = queue.popleft()
        if d1 > r:
            q, r = x, d1
        visited[x] = True
        for y, d2 in tree[x]:
            if not visited[y]:
                queue.append((y, d1 + d2))
    return q, r


v = int(input())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    p, *edgds, _ = MIIS()
    for i in range(len(edgds) // 2):
        tree[p].append((edgds[i * 2], edgds[i * 2 + 1]))

# 트리의 지름 끝점 찾기
x, _ = bfs(1)

# 트리의 지름
_, r = bfs(x)
print(r)
