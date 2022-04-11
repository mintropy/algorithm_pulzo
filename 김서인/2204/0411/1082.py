import sys

input = sys.stdin.readline

N = int(input())
price = {}
tmp = list(map(int, input().split()))
for i in range(N):
    price[i] = tmp[i]

M = int(input())
dp = ['-'] * (51)  # 그 돈으로 살 수 있는 제일 큰 방 번호

# 초기 세팅
for i in range(N):
    now_price = price[i]
    dp[now_price] = i

for i in range(min(price.values()) * 2, M + 1):
    for j in price.keys():
        now_price = price[j]
        if dp[i - now_price] != '-' and (i - now_price) >= 0:
            if dp[i] == '-':
                dp[i] = 0
            dp[i] = max(dp[i], dp[i - now_price] * 10 + j)

new_dp = []
for i in range(1, M+1):
    if dp[i] == '-':
        pass
    else:
        new_dp.append(dp[i])
print(max(new_dp))
