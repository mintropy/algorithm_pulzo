import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(y, x, ac, op):
    global N, max_value, min_value
    if y == N or x == N:
        return

    if y == 0 and x == 0:
        pass
    else:
        if board[y][x] in '+-*':
            op = board[y][x]
        else:
            ac = eval(f'{ac}{op}{board[y][x]}')

    if y == x == N-1:
        max_value = max(max_value, ac)
        min_value = min(min_value, ac)
        return

    dfs(y, x+1, ac, op)
    dfs(y+1, x, ac, op)


N = int(input())
board = [tuple(input().rstrip().split()) for _ in range(N)]

max_value, min_value = float('-inf'), float('inf')
dfs(0, 0, board[0][0], None)
print(max_value, min_value)
