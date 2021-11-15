"""
Title : 카드 구매하기 2
Link : https://www.acmicpc.net/problem/16194
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N = int(input())
prices = [0] + list(MIIS())

dp = prices[::]
dp[1] = prices[1]

# 지금 카드 개수
for card_count in range(1, N):
    price_now = dp[card_count]
    for additional_card_pack in range(1, N - card_count + 1):
        if dp[card_count + additional_card_pack] > price_now + prices[additional_card_pack]:
            dp[card_count + additional_card_pack] = price_now + prices[additional_card_pack]

print(dp[N])
