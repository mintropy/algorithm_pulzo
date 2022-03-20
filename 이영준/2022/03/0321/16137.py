"""
Title : 견우와 직녀
Link : https://www.acmicpc.net/problem/16137
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    arraies = [list(MIIS()) for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    
    possible_ojakgyo_pos = []
    ojakgyo_pos = []
    disable_cliff = [
        [0, 1], [1, 2], [2, 3], [0, 3]
    ]
    for i in range(N):
        for j in range(N):
            if arraies[i][j]:
                if arraies[i][j] >= 2:
                    ojakgyo_pos.append((i, j))
                continue
            cliff_dirs = []
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < N and not arraies[nx][ny]:
                    cliff_dirs.append(d)
            if len(cliff_dirs) >= 3 or cliff_dirs in disable_cliff:
                continue
            possible_ojakgyo_pos.append((i, j))
    
    min_time = 100_000
    for i, j in possible_ojakgyo_pos:
        arraies[i][j] = M
        visited = [[100_000] * N for _ in range(N)]
        queue = deque([(0, 0, 0)])
        while queue:
            x, y, t = queue.popleft()
            if x == N - 1 and y == N - 1:
                if min_time > t:
                    min_time = t
                continue
            if visited[x][y] <= t:
                continue
            visited[x][y] = t
            if arraies[x][y] >= 2:
                on_ojakgyo = True
            else:
                on_ojakgyo = False
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if not arraies[nx][ny]:
                        continue
                    elif arraies[nx][ny] == 1 and visited[nx][ny] > t:
                        queue.append((nx, ny, t + 1))
                    elif not on_ojakgyo:
                        term = arraies[nx][ny]
                        if (t + 1) % term:
                            next_open = ((t + 1) // term + 1) * term
                        else:
                            next_open = t + 1
                        if visited[nx][ny] > next_open:
                            queue.append((nx, ny, next_open))
        arraies[i][j] = 0
    print(min_time)

'''
8 2 
1 1 1 1 0 1 1 1 
1 1 0 1 0 1 0 1 
0 0 0 1 1 1 0 1 
0 0 0 0 0 0 0 1 
0 0 0 0 0 1 0 1 
0 0 0 0 0 1 1 1 
0 0 0 0 0 0 0 10 
0 0 0 0 0 0 1 1
ans : 20

5 10
1 1 2 3 1
1 1 0 0 1
13 0 0 0 1
1 1 1 1 1
1 1 1 1 1
ans : 15
'''
