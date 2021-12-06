"""
Title : 숫자카드
Link : https://www.acmicpc.net/problem/2591
"""


num = list(int(i) for i in input().strip())

# 카드는 1 ~ 34
dp = [0] * len(num)
dp[0] = 1

for i in range(1, len(num)):
    # 1자리수 카드로 추가하는 방법
    # 0 확인
    if num[i] != 0:
        dp[i] += dp[i - 1]
    
    # 2자리수가 가능한지 확인
    n = num[i - 1] * 10 + num[i]
    if 10 <= n <= 34:
        if i == 1:
            dp[i] += 1
        else:
            dp[i] += dp[i - 2]

print(dp[-1])