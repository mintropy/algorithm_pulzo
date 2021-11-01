"""
Title : 문자열 지옥에 빠진 호석
Link : https://www.acmicpc.net/problem/20166
"""

import sys
input = sys.stdin.readline


def search(string_now: str, x: int, y: int):
    global n, m, grid, dx, dy
    global loved_strings_set, strings_count, max_string_length
    # 신이 좋아하는 문자열인지
    if string_now in strings_count:
        strings_count[string_now] += 1
    else:
        strings_count[string_now] = 1
    # 최대 길이일때
    if len(string_now) == max_string_length:
        return
    # 아니라면 탐색
    for d in range(8):
        nx, ny = (x + dx[d]) % n, (y + dy[d]) % m
        search(string_now + grid[nx][ny], nx, ny)


n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]
loved_strings = [input().strip() for _ in range(k)]
loved_strings_set = set(loved_strings)
strings_count = {}
max_string_length = max([len(s) for s in loved_strings])

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0 ,-1, -1, -1)

for i in range(n):
    for j in range(m):
        search(grid[i][j], i, j)

print(*[strings_count.setdefault(s, 0) for s in loved_strings], sep='\n')


'''
# python TLE
def search(string_now: str, x: int, y: int):
    global n, m, grid, dx, dy
    global loved_strings_set, loved_strings_count, max_string_length
    # 신이 좋아하는 문자열인지
    if string_now in loved_strings:
        loved_strings_count[string_now] += 1
    # 최대 길이일때
    if len(string_now) == max_string_length:
        return
    # 아니라면 탐색
    for d in range(8):
        nx, ny = (x + dx[d]) % n, (y + dy[d]) % m
        search(string_now + grid[nx][ny], nx, ny)


n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]
loved_strings = [input().strip() for _ in range(k)]
loved_strings_set = set(loved_strings)
loved_strings_count = {s: 0 for s in loved_strings}
max_string_length = max([len(s) for s in loved_strings])

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0 ,-1, -1, -1)

for i in range(n):
    for j in range(m):
        search(grid[i][j], i, j)

print(*[loved_strings_count[s] for s in loved_strings], sep='\n')
'''