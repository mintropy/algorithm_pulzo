import sys
input = sys.stdin.readline
d = {
    'E': [0, 1],
    'S': [1, 0],
    'W': [0, -1],
    'N': [-1, 0],
}

N, M, R = map(int, input().split())
board = []
ans = [['S'] * M for _ in range(N)]
fallen = 0
for _ in range(N):
    board.append(tuple(map(int, input().split())))

for _ in range(R):
    Y, X, D = input().split()
    Y, X = int(Y) - 1, int(X) - 1

    curr_y, curr_x = Y, X
    cnt = board[curr_y][curr_x]
    if ans[curr_y][curr_x] == 'S':
        ans[curr_y][curr_x] = 'F'
        fallen += 1
        cnt -= 1
        curr_y += d[D][0]
        curr_x += d[D][1]
        while cnt > 0 and 0 <= curr_y < N and 0 <= curr_x < M:
            if ans[curr_y][curr_x] == 'S':
                fallen += 1
                cnt = max(cnt, board[curr_y][curr_x])
            cnt -= 1
            ans[curr_y][curr_x] = 'F'
            curr_y += d[D][0]
            curr_x += d[D][1]

    
    Y, X = map(int, input().split())
    ans[Y - 1][X - 1] = 'S'

print(fallen)
for i in range(N):
    print(*ans[i])