import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]

zero_list = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_list.append((i, j))


def candidates(y, x):
    ret = []
    visit = [None] + [False]*9  # 1~9 사용

    for i in range(y//3*3, y//3*3+3):
        for j in range(x//3*3, x//3*3+3):
            visit[board[i][j]] = True

    for i in range(9):
        visit[board[y][i]] = True

    for i in range(9):
        visit[board[i][x]] = True

    for i in range(1, 10):
        if not visit[i]:
            ret.append(i)

    return ret


def go(cnt, fr):
    if cnt == 0:
        return True

    i, j = zero_list[fr]
    candidate = candidates(i, j)
    for n in candidate:
        board[i][j] = n
        if go(cnt-1, fr+1):
            return True
        board[i][j] = 0
    return False


go(len(zero_list), 0)
for v in board:
    print(*v, sep='')
