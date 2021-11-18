import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

INF = 10001

N = int(input())
arr = [0] + list(MIIS())

dp = [INF] * (N+1)

for i in range(N+1):
    dp[i] = arr[i]

    for j in range(i):
        dp[i] = min(dp[i], dp[i-j] + arr[j]) # 바로 j개 카드 세트 사는 것, 다른 세트들 더해서 사는 것

print(dp[N])