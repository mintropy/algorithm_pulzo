"""
Title : 소문난 칠공주
Link : https://www.acmicpc.net/problem/1941
"""

import sys
input = sys.stdin.readline


def dfs(group_now: int, som_pa_now: int):
    global students, students_check, possible_seven_princess, seven_princess_now, dx, dy
    # 불가능한 경우 / 추가로 더 모아도 솜파 4명 못만듬
    if 7 - group_now + som_pa_now < 4:
        return
    # 7명 모두 탐색
    if group_now == 7:
        if som_pa_now >= 4:
            possible_seven_princess.add(tuple(sorted(seven_princess_now)))
        return
    # 각 위치마다 가능한자리 따로 구해보기
    possible_seat = set()
    for x, y in seven_princess_now:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and not students_check[nx][ny]:
                possible_seat.add((nx, ny))
    # 각 가능한 자리 하나씩 추가하며 탐색
    for x, y in possible_seat:
        students_check[x][y] = True
        seven_princess_now.append((x, y))
        if students[x][y] == 'S':
            dfs(group_now + 1, som_pa_now + 1)
        else:
            dfs(group_now + 1, som_pa_now)
        students_check[x][y] = False
        seven_princess_now.pop()


students = [input().strip() for _ in range(5)]
students_check = [[False] * 5 for _ in range(5)]

possible_seven_princess = set()
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
seven_princess_now = []

for i in range(5):
    for j in range(5):
        # 솜파 한명 기준으로 탐색하면 다시 그 사람 속하는 그룹으로 탐색 필요 ㄴㄴ
        if students[i][j] == 'S':
            seven_princess_now.append((i, j))
            students_check[i][j] = True
            dfs(1, 1)
            seven_princess_now.pop()

print(len(possible_seven_princess))


'''
Counter Example
SSYYY
SYYYY
YYSYY
YYYYY
YYYYY
ans : 23
'''