'''
마리오 파티

'''
import sys
input = sys.stdin.readline

while 1:
    input_list = list(map(int,input().split()))
    if input_list[0] == 0:
        break
    N, S, T = input_list[0], input_list[1], input_list[2]

    board = []

    while len(board) < N:
        board.extend(list(map(int,input().split())))
    INF = -987654321  
    dp = [[INF] * (N+1) for _ in range(T)]
    
    for i in range(S):
        dp[0][i] = board[i]
    
    for i in range(T-1):
        for j in range(N):
            if dp[i][j] != INF:
                for k in range(1,S+1):
                    if j + k >= N:
                        if dp[i+1][N] < dp[i][j]:
                            dp[i+1][N] = dp[i][j]
                    else:
                        if dp[i+1][j+k] < dp[i][j] + board[j+k]:
                            dp[i+1][j+k] = dp[i][j] + board[j+k]

    print(dp[-1][-1])        

