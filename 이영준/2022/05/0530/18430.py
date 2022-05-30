"""
Title : 무기 공학
Link : https://www.acmicpc.net/problem/18430
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search(x: int, y: int):
    global N, M, my_map, visited
    if x == N:
        return 0
    _x, _y = get_next_pos(x, y)
    max_points = search(_x, _y)
    if visited[x][y]:
        return max_points
    for d in range(4):
        if visited[x][y] or not check_direction(x, y, d):
            continue
        _point = get_points(x, y, d, True)
        _x, _y = get_next_pos(x, y)
        _next_point = search(_x, _y)
        if max_points < _point + _next_point:
            max_points = _point + _next_point
        get_points(x, y, d, False)
    return max_points


def get_next_pos(x: int, y: int) -> tuple:
    global N, M
    y += 1
    if y == M:
        x += 1
        y = 0
    return x, y


def check_direction(x: int, y: int, d: int) -> bool:
    global N, M, visited, direction
    for dx, dy in direction[d]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny]:
                return False
        else:
            return False
    return True


def get_points(x: int, y: int, d: int, mode: bool) -> bool:
    global N, M, my_map, visited, direction
    point = my_map[x][y] * 2
    visited[x][y] = mode
    for dx, dy in direction[d]:
        nx, ny = x + dx, y + dy
        point += my_map[nx][ny]
        visited[nx][ny] = mode
    return point


if __name__ == "__main__":
    N, M = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    direction = {
        0: ((-1, 0), (0, 1)),
        1: ((0, 1), (1, 0)),
        2: ((1, 0), (0, -1)),
        3: ((0, -1), (-1, 0)),
    }
    print(search(0, 0))
