import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(board, visit, y, x, color):
    R, C = len(board), len(board[0])

    if y < 0 or y >= R or x < 0 or x >= C:
        return 0

    if visit[y][x]:
        return 0

    if board[y][x] != color:
        return 0

    visit[y][x] = 1

    d_pos = ((-1, 0), (0, 1), (1, 0), (0, -1))

    ret = 1
    for dy, dx in d_pos:
        ret += dfs(board, visit, y+dy, x+dx, color)
    return ret


C, R = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
visit = [[0]*C for _ in range(R)]
w_ans = 0
b_ans = 0
for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            color = board[i][j]
            tmp = dfs(board, visit, i, j, color)
            if color == 'W':
                w_ans += tmp**2
            else:
                b_ans += tmp**2

#print(*visit, sep='\n')
#print(*board, sep='\n')
print(w_ans, b_ans)
