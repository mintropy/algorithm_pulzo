"""
Title : 화산 쇄설류
Link : https://www.acmicpc.net/problem/16569
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == '__main__':
    M, N, V = MIIS()
    X, Y = MIIS()
    heights = [[0 for _ in range(N + 1)]] + [[0] + list(MIIS()) for _ in range(M)]
    volcanos = sorted([tuple(MIIS()) for _ in range(V)], key=lambda x: x[2])

    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    dusts = [[100_000] * (N + 1) for _ in range(M + 1)]
    idx = 1
    time = volcanos[0][2]
    stack = [(volcanos[0][:2])]
    while stack:
        while idx < V:
            if volcanos[idx][2] == time:
                stack.append(volcanos[idx][:2])
                idx += 1
            else:
                break
        next_stack = []
        for x, y in stack:
            if time >= dusts[x][y] :
                continue
            dusts[x][y] = time
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 1 <= nx <= M and 1 <= ny <= N:
                    if time + 1 < dusts[nx][ny]:
                        next_stack.append((nx, ny))
        stack = next_stack[::]
        time += 1
    for x, y, _ in volcanos:
        heights[x][y] = -1

    max_heights = heights[X][Y]
    ans_time = 0
    time = 0
    pos = [(X, Y)]
    while pos:
        next_pos = []
        for x , y in pos:
            if heights[x][y] == -1 or time >= dusts[x][y]:
                continue
            if max_heights < heights[x][y]:
                max_heights = heights[x][y]
                ans_time = time
            heights[x][y] = -1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 1 <= nx <= M and 1 <= ny <= N:
                    if heights[nx][ny] != -1:
                        next_pos.append((nx, ny))
        pos = next_pos[::]
        time += 1
    print(max_heights, ans_time)

'''
Count Example
3 3 2
3 1
1000 0 0
0 0 0
0 0 0
2 1 100
2 2 100
ans : 1000 6
'''
