import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


H, W = map(int, input().split())
S = map(int, input().split())

board = [[0]*W for _ in range(H)]

for i, v in enumerate(S):
    for j in range(v):
        board[j][i] = 1

print(*board, sep='\n')

ans = 0
st = []
flag = False
for i in range(H):
    for j in range(W):
        if flag:
            if board[i][j] == 0:
                st.append((i, j))
            else:
                if st:
                    ans += len(st)
                    #print(st, i, j)
                    st.clear()
        else:
            if board[i][j] == 1:
                flag = True
    flag = False
    st.clear()

print(ans)
