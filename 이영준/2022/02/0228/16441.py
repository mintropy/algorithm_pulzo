"""
Title : 아기돼지와 늑대
Link : https://www.acmicpc.net/problem/16441
"""

from collections import deque
import sys
input = sys.stdin.readline


def solution() -> None:
    N, M = map(int, input().split())
    my_map = [list(input().strip()) for _ in range(N)]

    queue = deque([])
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == '.':
                my_map[i][j] = 'P'
            elif my_map[i][j] == 'W':
                queue.append((i, j))

    visited = [[False] * M for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if my_map[nx][ny] == 'P':
                my_map[nx][ny] = '.'
                queue.append((nx, ny))
            elif my_map[nx][ny] == '+':
                while True:
                    nnx, nny = nx + dx[d], ny + dy[d]
                    if my_map[nnx][nny] in ('.', 'W'):
                        break
                    elif my_map[nnx][nny] == 'P':
                        my_map[nnx][nny] = '.'
                        queue.append((nnx, nny))
                        break
                    elif my_map[nnx][nny] == '+':
                        nx, ny = nnx, nny
                    elif my_map[nnx][nny] == '#':
                        queue.append((nx, ny))
                        break

    for line in my_map:
        print(''.join(line))
    return None


solution()
