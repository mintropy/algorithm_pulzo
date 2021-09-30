from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(y, x):
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    visit = [[0]*(M+1) for _ in range(N+1)]
    visit_b_wall = [[0]*(M+1) for _ in range(N+1)]
    dq = collections.deque()
    dq.append((y, x, True, 1))
    while dq:
        tmp_y, tmp_x, b_wall, cnt = dq.popleft()

        if tmp_y < 1 or tmp_x < 1 or tmp_y > N or tmp_x > M:
            continue

        if tmp_y == N and tmp_x == M:
            return cnt

        if board[tmp_y][tmp_x] == '1':
            if b_wall:
                b_wall = False
            else:
                continue

        if b_wall:
            if visit[tmp_y][tmp_x] == 1:
                continue
        else:
            if visit_b_wall[tmp_y][tmp_x] == 1:
                continue

        if b_wall:
            visit[tmp_y][tmp_x] = 1
        else:
            visit_b_wall[tmp_y][tmp_x] = 1

        for i in range(4):
            dq.append((tmp_y+dy[i], tmp_x+dx[i], b_wall, cnt+1))

    return -1


N, M = map(int, input().split())
board = [('X',)*(M+1)] + [('X',)+tuple(input().rstrip()) for _ in range(N)]

print(bfs(1, 1))
