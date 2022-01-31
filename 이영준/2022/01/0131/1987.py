"""
Title : 알파벳
Link : https://www.acmicpc.net/problem/1987
"""

import sys
input = sys.stdin.readline


def dfs(alpabet_check: list, count: int, x: int, y: int):
    global dx, dy, max_count, visited
    if count == 26:
        max_count = 26
        return True
    elif max_count < count:
        max_count = count
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            idx = ord(grid[nx][ny]) - 65
            if not alpabet_check[idx]:
                alpabet_check[idx] = True
                dfs(alpabet_check, count + 1, nx, ny)
                alpabet_check[idx] = False
    return False


R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
max_count = 0
visited = [[False] * C for _ in range(R)]

check = [False] * 26
check[ord(grid[0][0]) - 65] = True
dfs(check, 1, 0, 0)
print(max_count)
