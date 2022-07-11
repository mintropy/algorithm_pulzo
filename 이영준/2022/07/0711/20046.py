"""
Title : Road Reconstruction
Link : https://www.acmicpc.net/problem/20046
"""

from heapq import heappush, heappop
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    city = [list(MIIS()) for _ in range(N)]
    if city[0][0] == -1 or city[-1][-1] == -1:
        print(-1)
        exit()
    cost = [[2_000_000] * M for _ in range(N)]
    heap = [(city[0][0], 0, 0)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    ans = -1
    while heap:
        c, x, y = heappop(heap)
        if x == N - 1 and y == M - 1:
            ans = c
            break
        if cost[x][y] <= c:
            continue
        cost[x][y] = c
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                _c = city[nx][ny]
                if _c != -1 and cost[nx][ny] > x + _c:
                    heappush(heap, (c + _c, nx, ny))
    print(ans)

"""
5 5
0 0 0 0 0
1 1 1 1 1
1 1 1 1 1
0 0 0 0 -1
2 2 2 2 2
"""
