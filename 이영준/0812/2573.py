"""
Title : 빙산
Link : https://www.acmicpc.net/problem/2573
"""

import sys, collections
input = sys.stdin.readline


def find_ice(n: int, m: int, iceberg: list) -> list:
    global dx, dy
    ice = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if iceberg[i][j]:
                ice.append((i, j, iceberg[i][j]))
    return ice


def next_year(n: int, m: int, ice: list, iceberg: list) -> list:
    global dx, dy
    new_ice = []
    # 빙산 중 한 부분에서 시작, 변경 되는 부분 확인
    queue = collections.deque([ice[0]])
    visited = [[False] * m for _ in range(n)]
    visited[ice[0][0]][ice[0][1]] = True
    while queue:
        x, y, h = queue.popleft()
        zero_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not iceberg[nx][ny]:
                zero_count += 1
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, iceberg[nx][ny]))
        # 낮아지는 높이 확인
        h -= zero_count
        if h < 0:
            h = 0
        new_ice.append((x, y, h))
    return new_ice


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 모든 빙산 조각 확인
ice = find_ice(n, m, iceberg)
year = 0

while True:
    # 더이상 빙산이 없으면 종료
    if not ice and year >= 0:
        print(0)
        break
    # 1년이 지나서 녹게된 빙산
    # 다음 년도 탐색할 때 두 덩어리 이상인 경우
    new_ice = next_year(n, m, ice, iceberg)
    if len(ice) != len(new_ice):
        print(year)
        break
    # 다음년도 탐색에도 한 덩어리인경우
    year += 1
    ice = []
    for x, y, h in new_ice:
        iceberg[x][y] = h
        if h:
            ice.append((x, y, h))