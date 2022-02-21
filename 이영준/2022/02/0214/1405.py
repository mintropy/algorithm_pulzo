"""
Title : 미친 로봇
Link : https://www.acmicpc.net/problem/1405
"""

import sys

input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
visited = [[False] * 30 for _ in range(30)]


def solution() -> None:
    """Main solution function"""
    total, E, W, S, N = map(int, input().split())
    moves = (N / 100, E / 100, S / 100, W / 100)
    print(dfs((0, 0), total, 0, moves))


def dfs(pos_now: tuple, total: int, count: int, moves: tuple) -> float:
    """Back tracking function

    Parameters
    ----------
    pos_now : tuple
    total : int
        total moves limit
    count : int
        moves count
    moves : tuple

    Returns
    -------
    float
        probability
    """
    global dx, dy, visited
    if count == total:
        return 1
    x, y = pos_now
    visited[x][y] = True
    prob = 0
    for d in range(4):
        nx, ny = pos_now[0] + dx[d], pos_now[1] + dy[d]
        if not visited[nx][ny]:
            prob += moves[d] * dfs((nx, ny), total, count + 1, moves)
    visited[x][y] = False
    return prob


solution()
