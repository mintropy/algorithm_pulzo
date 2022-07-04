"""
Title : 불!
Link : https://www.acmicpc.net/problem/4179
"""

from collections import deque
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    R, C = map(int, input().split())
    maze = [input().strip() for _ in range(R)]
    fire_time = [[-1] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    fires = deque([])
    queue = deque([])
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "J":
                queue.append((0, i, j))
            elif maze[i][j] == "F":
                fires.append((0, i, j))
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    ans = -1
    while fires:
        time, x, y = fires.popleft()
        if fire_time[x][y] >= 0:
            continue
        fire_time[x][y] = time
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] != "#":
                    fires.append((time + 1, nx, ny))
    while queue:
        time, x, y = queue.popleft()
        if x < 0 or x >= R or y < 0 or y >= C:
            ans = time
            break
        if -1 != fire_time[x][y] <= time or visited[x][y]:
            continue
        visited[x][y] = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and maze[nx][ny] != "#":
                    queue.append((time + 1, nx, ny))
            else:
                queue.append((time + 1, nx, ny))
    print(ans if ans != -1 else "IMPOSSIBLE")

"""
5 5
.....
.FFF.
.FJF.
.FFF.
.....
"""
