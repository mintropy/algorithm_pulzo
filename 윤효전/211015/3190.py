import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isTail(y, x, board):
    if board[y][x] == 2:
        return True
    return False


N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    R, C = map(lambda x: int(x)-1, input().split())
    board[R][C] = 1

L = int(input())
actions = []
for _ in range(L):
    X, C = input().rstrip().split()
    X = int(X)
    actions.append((X, C))

pos_y, pos_x = 0, 0
direction = 'R'

d_pos = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
}

d_graph = {
    'R': {'L': 'U', 'D': 'D'},
    'D': {'L': 'R', 'D': 'L'},
    'L': {'L': 'D', 'D': 'U'},
    'U': {'L': 'L', 'D': 'R'},
}
player_pos_list = deque()
player_pos_list.append((0, 0))
board[0][0] = 2
ans = 0
cur = 0
while True:
    pos_y += d_pos[direction][0]
    pos_x += d_pos[direction][1]
    ans += 1
    if pos_y < 0 or pos_y >= N or pos_x < 0 or pos_x >= N:
        break
    if isTail(pos_y, pos_x, board):
        break
    if board[pos_y][pos_x] != 1:
        tmp_y, tmp_x = player_pos_list.popleft()
        board[tmp_y][tmp_x] = 0
    board[pos_y][pos_x] = 2
    player_pos_list.append((pos_y, pos_x))
    if cur < len(actions) and ans == actions[cur][0]:
        direction = d_graph[direction][actions[cur][1]]
        cur += 1

print(ans)
