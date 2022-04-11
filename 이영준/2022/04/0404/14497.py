"""
Title : 주난의 난(難)
Link : https://www.acmicpc.net/problem/14497
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    x1, y1, x2, y2 = MIIS()
    classroom = [list(input().strip()) for _ in range(N)]
    count = 0
    waves = [(x1 - 1, y1 - 1)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while True:
        if (x2 - 1, y2 - 1) in waves:
            print(count)
            break
        next_waves = []
        while waves:
            x, y = waves.pop()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if classroom[nx][ny] == '1' or classroom[nx][ny] == '#':
                        classroom[nx][ny] = '*'
                        next_waves.append((nx, ny))
                    elif classroom[nx][ny] == '0':
                        classroom[nx][ny] = '*'
                        waves.append((nx, ny))
        waves = next_waves[::]
        count += 1
