"""
Title : 비트코인은 신이고 나는 무적이다
Link : https://www.acmicpc.net/problem/23257
"""

# https://stackoverflow.com/questions/52108901/xor-operation-on-three-values

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, m = MIIS()
montly_bong = list(map(lambda x: abs(int(x)), input().split()))

last_montly_bong = set(montly_bong)
for _ in range(m - 1):
    last_montly_bong = set(i ^ j for i in montly_bong for j in last_montly_bong)

print(max(last_montly_bong))


'''
# AC
n, m = MIIS()
montly_bong = list(MIIS())
dp = [[False] * 1024 for _ in range(m)]
# 월봉값을 절댓값으로 저장 & 월봉값 있는 위치에 표시
for i in range(n):
    montly_bong[i] = abs(montly_bong[i])
    dp[0][montly_bong[i]] = True

# 2 ~ m개 선택하는 경우의 수 탐색
for i in range(1, m):
    # 각각 위치 탐색
    for bong in montly_bong:
        for j in range(1024):
            dp[i][j ^ bong] |= dp[i - 1][j]

for i in range(1023, -1, -1):
    if dp[m - 1][i]:
        print(i)
        break
'''

'''
# TLE
n, m = MIIS()
montly_bong = list(MIIS())
# 월봉값을 절댓값으로 저장
for i in range(n):
    montly_bong[i] = abs(montly_bong[i])

if m == 1:
    print(max(montly_bong))
else:
    dp = montly_bong[::]
    # 초기 XOR 값 설정
    for i in range(n):
        price_last = dp[i]
        price_next = 0
        for j in range(i + 1):
            if price_next < montly_bong[i] ^ montly_bong[j]:
                price_next = montly_bong[i] ^ montly_bong[j]
        dp[i] = price_next
    # 3개에서 n개 선택
    for _ in range(3, m + 1):
        for i in range(n):
            price_last = dp[i]
            price_next = 0
            for j in range(i + 1):
                price_tmp = montly_bong[i] ^ montly_bong[j]
                if price_next < price_last | price_tmp:
                    price_next = price_last | price_tmp
            dp[i] = price_next
    print(max(dp))
'''
