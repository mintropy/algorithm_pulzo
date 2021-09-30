import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

dp = [[0]*(N+1) for _ in range(12)]

for i in range(2, 11):
    dp[i][1] = 1

#print(*dp, sep='\n')

for j in range(2, N+1):
    for i in range(1, 11):
        dp[i][j] = (dp[i-1][j-1] + dp[i+1][j-1]) % 1000000000

res = 0
for i in range(1, 11):
    res += dp[i][N] % 1000000000
    res %= 1000000000

#print(*dp, sep='\n')
print(res)