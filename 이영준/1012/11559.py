"""
Title : Puyo Puyo
Link : https://www.acmicpc.net/problem/11559
"""

import collections
import sys
input = sys.stdin.readline


field = [list(input().strip()) for _ in range(12)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

combo = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    puyo_pop = False
    # 한 번에 제거가능한 뿌요 탐색, 제거
    for i in range(11, -1, -1):
        for j in range(6):
            if not visited[i][j] and field[i][j] != '.':
                # 탐색 큐
                queue = collections.deque([(i, j)])
                # 탐색 종료 후 터트리기 위한 스택
                stack = []
                color_now = field[i][j]
                while queue:
                    x, y = queue.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    stack.append((x, y))
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if field[nx][ny] == color_now and not visited[nx][ny]:
                                queue.append((nx, ny))
                # 탐색 종료, 한번에 없어질 수 있는지
                if len(stack) >= 4:
                    puyo_pop = True
                    for x, y in stack:
                        field[x][y] = '.'
    # 제거한 뿌요 없으면 종료
    if not puyo_pop:
        break
    # 아니라면 뿌요들 모두 떨어트리기
    combo += 1
    for j in range(6):
        down, up = 11, 11
        while up >= 0:
            if field[up][j] == '.' or up >= down:
                up -= 1
            elif field[down][j] != '.':
                down -= 1
            else:
                field[up][j], field[down][j] = field[down][j], field[up][j]
                up -= 1
                down -= 1

print(combo)
