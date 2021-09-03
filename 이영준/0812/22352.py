"""
Title : 항체 인식
Link : https://www.acmicpc.net/problem/22352
"""


import sys, collections
input = sys.stdin.readline


def check_all(n: int, m: int, before: list, after: list) -> bool:
    global diff, pos
    # befor/after를 비교하며 확인
    # 1. 변한 부분이 없으면 (== 우연히 같은 번호로 변하면) True로 반환
    # 2. 변하는 숫자를 확인, 2가지 이상 숫자가 변하면 False
    check = (-1, -1)
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                diff[i][j] = True
                pos.append((i, j))
                if check == (-1, -1):
                    check = (before[i][j], after[i][j])
                elif check[0] != before[i][j] or check[1] != after[i][j]:
                    return False
    return True


def bfs_same_num(n: int, m: int, diff: list, pos: list) -> bool:
    global before, dx, dy
    # 한 점에서 시작, diff에서 Flase이고
    # 이동할 수 있는 공간중에 같은 숫자인 경우가 있으면 Flase
    deque = collections.deque([pos[0]])
    num = before[pos[0][0]][pos[0][1]]
    visited = [[False] * m for _ in range(n)]
    visited[pos[0][0]][pos[0][1]] = True
    while deque:
        x, y = deque.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and diff[nx][ny]:
                    visited[nx][ny] = True
                    deque.append((nx, ny))
                elif not diff[nx][ny] and before[nx][ny] == num:
                    return False
    return True


def bfs_check_pos(n: int, m: int, diff: list, pos: list) -> bool:
    global dx, dy
    deque = collections.deque([pos[0]])
    diff[pos[0][0]][pos[0][1]] = False
    # 변화가 있었던 부분 중 한곳을 잡아 모두 이동 가능한지 확인
    while deque:
        x, y = deque.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if diff[nx][ny]:
                    diff[nx][ny] = False
                    deque.append((nx, ny))
    # 변화가 있었던 부분을 확인, 한번에 이동 불가능하면 False
    for x, y in pos:
        if diff[x][y]:
            return False
    return True


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 바뀐 부분 확인
diff = [[False] * m for _ in range(n)]
pos = []

# 모두 탐색하며, 다른 숫자가 변했을 때
if not check_all(n, m, before, after):
    print('NO')
# 우연히 변한곳이 없을 때
elif not pos:
    print('YES')
# 변하지 않은 칸이 있을 때
elif not bfs_same_num(n, m, diff, pos):
    print('NO')
# bfs 탐색
elif bfs_check_pos(n, m, diff, pos):
    print('YES')
# bfs결과 False일 때
else:
    print('NO')



'''
count example
4 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
2 2 3 4
2 2 3 4
2 2 3 4
1 2 3 4
ans : NO

3 4
2 2 1 1
3 2 1 1
2 3 2 1
1 1 1 1
3 4 1 1
2 3 2 1
ans : NO
'''