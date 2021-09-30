import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]

dp = [[0] * 3 for _ in range(N+2)]

for i in range(2, N+2):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = max(dp[i-1][0]+S[i-2], dp[i-1][2]+S[i-2])
    dp[i][2] = dp[i-1][0] + S[i-2]

print(max(dp[N+1]))
