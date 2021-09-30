import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
board = [[int(n) for n in input().split()] for _ in range(N)]

d_yx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(h, chk, y, x):
    if 0 <= y < N and 0 <= x < N and chk[y][x] == 0 and board[y][x] > h:
        chk[y][x] = 1
        for dy, dx in d_yx:
            tmpy, tmpx = y+dy, x+dx
            dfs(h, chk, tmpy, tmpx)
    else:
        return

res = 0
for h in range(0, 101):
    chk = [[0]*N for _ in range(N)]
    area_cnt = 0
    for y in range(N):
        for x in range(N):
            if chk[y][x] == 0 and board[y][x] > h:
                dfs(h, chk, y, x)
                area_cnt += 1
    res = max(res, area_cnt)
print(res)