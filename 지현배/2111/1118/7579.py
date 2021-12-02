import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = sum(cost)
dp = [0] * (total + 1)

for i in range(N):
    for j in range(total, -1, -1):
        if dp[j]:
            dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + memory[i])
    dp[cost[i]] = max(dp[cost[i]], memory[i])

for i in range(total + 1):
    if dp[i] >= M:
        print(i)
        break