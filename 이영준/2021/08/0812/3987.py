"""
Title : 보이저 1호
Link : https://www.acmicpc.net/problem/3987
"""


import sys
input = sys.stdin.readline


def move(r, c, d):
    global n, m, space, dx, dy
    time = 0
    x, y = r, c
    visited = [[False] * m for _ in range(n)]
    while True:
        # 공간 밖으로 벗어나면 종료
        if x < 0 or x >= n or y < 0 or y >= m:
            break
        # 블랙홀을 만나면 종료
        if space[x][y] == 'C':
            break
        # 행성을 만난 경우 방향 전환
        if space[x][y] == '/' or space[x][y] == '\\':
            d = change_direction(x, y, d)
        # 이미 방문했으면 무한 루프 확인
        if visited[x][y]:
            is_loop = check_inifite_loop(x, y, d, visited)
            if is_loop == 'Voyager':
                return is_loop
            elif is_loop > 0:
                return time + is_loop
        visited[x][y] = True
        time += 1
        x += dx[d]
        y += dy[d]
    return time


def change_direction(x, y, d):
    global space
    if space[x][y] == '/':
        # 방향 d가 0<->1 2<->3
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        else:
            return 2
    elif space[x][y] == '\\':
        # 방향 d가 0<->3 또는 1<->2
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        else:
            return 0

def check_inifite_loop(x, y, d, visited):
    global n, m, space, dx, dy
    # 해당 칸을 방문했으므로 경우의 수는 2가지
    # 이전 경로와 교차해서 지나가는 경우
    # 무한 루프에 빠지는 경우
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return 0
    if not visited[nx][ny]:
        return 0
    else:
        # 한칸 앞이 방문한 칸이기는 하지만, 무한 루프임을 증명하지 못함
        # 해당 칸에서 시작, 다시 해당 칸으로 오게되면 무한루프
        # 무한 루프만 확인하는 것이므로, 칸 방문한것을 고려하지 않고
        # 범위 벗어나는 경우, 블랙홀 빠지게 되면 해당 시간만큼 return
        # 다시 시작점 x, y에 돌아오면 Voyager return
        time = 1
        while True:
            # 종료 조건
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return time
            if nx == x and ny == y:
                return 'Voyager'
            if space[nx][ny] == 'C':
                return time
            # 행성에 도착한 경우
            if space[nx][ny] == '/' or space[nx][ny] == '\\':
                d = change_direction(nx, ny, d)
            # 그 외의 경우 visited 상관없이 탐색
            time += 1
            nx += dx[d]
            ny += dy[d]


n, m = map(int, input().split())
space = [list(input().strip()) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

max_time = ('d', 0)
d = ['U', 'R', 'D', 'L']
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# U, R, D, L 순서로 탐색
for i in range(4):
    time = move(r, c, i)
    if time == 'Voyager':
        print(d[i], time, sep = '\n')
        break
    if time > max_time[1]:
        max_time = (d[i], time)
else:
    print(*max_time, sep = '\n')