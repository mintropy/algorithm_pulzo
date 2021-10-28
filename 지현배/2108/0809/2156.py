import sys
ipt = sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]
if n > 2:
    dp = [
        wine[0], 
        wine[0] + wine[1], 
        max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
        ] + [0 for _ in range(n - 3)]
    for idx in range(3, n):
        dp[idx] = max(
        dp[idx - 1], 
        dp[idx - 2] + wine[idx], 
        dp[idx - 3] + wine[idx - 1] + wine[idx])
    print(dp[-1])
else:
    print(sum(wine))