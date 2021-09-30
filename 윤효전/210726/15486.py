import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    t, p = map(int, input().split())
    S.append((t, p))


dp = [0]*(N+1)
current_max = 0
res = 0
for i in range(1, N+1):
    current_max = max(current_max, dp[i-1])
    t, p = S[i-1]
    if i-1+t > N:
        continue
    dp[i-1+t] = max(current_max + p, dp[i-1+t])

res = max(current_max, dp[N])
print(res)
