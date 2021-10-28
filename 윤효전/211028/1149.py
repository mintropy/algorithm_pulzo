import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(2)]

dp[0][0], dp[0][1], dp[0][2] = S[0][0], S[0][1], S[0][2]
for i in range(1, N):
    dp[1][0] = S[i][0] + min(dp[0][1], dp[0][2])
    dp[1][1] = S[i][1] + min(dp[0][0], dp[0][2])
    dp[1][2] = S[i][2] + min(dp[0][0], dp[0][1])
    dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

print(min(dp[1]))
