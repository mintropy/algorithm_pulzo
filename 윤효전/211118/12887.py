import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def dfs(board, y, x, cnt):
    global N
    
    if x == N-1:
        return 1
    if board[y][x+1] == '.':
        return 1 + dfs(board, y, x+1, cnt+1)
    else:
        if y == 0 and board[y+1][x] == '.':
            return 1 + dfs(board, y+1, x, cnt+1)
        elif y == 1 and board[y-1][x] == '.':
            return 1 + dfs(board, y-1, x, cnt+1)
        else:
            pass

N = int(input())

board = []
for i in range(2):
    board.append(input().rstrip())
    
total = board[0].count('.') + board[1].count('.')
ans = float('inf')

if board[0][0] == '.':
    ans = dfs(board, 0, 0, 1)
    
if board[1][0] == '.':
    ans = min(ans, dfs(board, 1, 0, 1))
    
print(total - ans)