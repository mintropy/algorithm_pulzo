import sys
input = sys.stdin.readline
N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
MAX = N * 1000
dp = [[MAX, MAX, MAX] for _ in range(N)]
dp[0] = RGB[0]
for i in range(1, N):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + RGB[i][j]
print(min(dp[-1]))