"""
Title : 일루미네이션
Link : https://www.acmicpc.net/problem/5547
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def count_walls(x: int, y: int) -> int:
    global walls, delta
    count = 0
    for dx, dy in delta[x % 2]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= H + 1 and 0 <= ny <= W + 1:
            if walls[nx][ny]:
                count += 1
    return count


if __name__ == "__main__":
    W, H = MIIS()
    walls = (
        [[0] * (W + 2)] + [[0] + list(MIIS()) + [0] for _ in range(H)] + [[0] * (W + 2)]
    )
    visited = [[False] * (W + 2) for _ in range(H + 2)]
    delta = [
        [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
        [(-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)],
    ]
    ans = 0
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        ans += count_walls(x, y)
        for dx, dy in delta[x % 2]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= H + 1 and 0 <= ny <= W + 1:
                if not walls[nx][ny]:
                    queue.append((nx, ny))
    print(ans)
