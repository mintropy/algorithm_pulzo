import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

C, R = map(int, input().split())
board = [tuple(input().rstrip()) for _ in range(R)]

def find_start_end_pos(board):
    start_y, start_x, end_y, end_x = None, None, None, None
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'C':
                if start_y == None:
                    start_y, start_x = i, j
                else:
                    end_y, end_x = i, j
                    return start_y, start_x, end_y, end_x

start_y, start_x, end_y, end_x = find_start_end_pos(board)

visit = [[float('inf')]*C for _ in range(R)]

def bfs(board, visit, start_y, start_x, end_y, end_x):
    R, C = len(board), len(board[0])
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    dq = deque()
    dq.append((start_y, start_x, 0, None))
    visit[start_y][start_x] = -1
    while dq:
        now_y, now_x, cnt, direct = dq.popleft()
        for i in range(4):
            if 0 > now_y+dy[i] or now_y+dy[i] >= R or 0 > now_x+dx[i] or now_x+dx[i] >= C:
                continue
            if board[now_y+dy[i]][now_x+dx[i]] == '*':
                continue
            
            next_cnt = cnt
            if direct != None and direct != i:
                next_cnt += 1
                    
            if visit[now_y+dy[i]][now_x+dx[i]] < next_cnt:
                continue

            visit[now_y+dy[i]][now_x+dx[i]] = next_cnt
            dq.append((now_y+dy[i], now_x+dx[i], next_cnt, i))
    
    return visit[end_y][end_x]

print(bfs(board, visit, start_y, start_x, end_y, end_x))