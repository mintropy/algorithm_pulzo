"""
Title : 인형들
Link : https://www.acmicpc.net/problem/15954
"""

import decimal
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def calc_variation(nums, avg):
    variation = decimal.Decimal(0)
    for num in nums:
        variation += (num - avg) ** 2
    return variation / decimal.Decimal(len(nums))


N, K = MIIS()
dolls = list(MIIS())
for i in range(N):
    dolls[i] = decimal.Decimal(dolls[i])

standard_deviations = []

for i in range(N - K + 1):
    # K개 이상 연속 확인
    for j in range(i + K, N + 1):
        dolls_now = dolls[i:j]
        avg = decimal.Decimal(str(sum(dolls_now) / K))
        variation = calc_variation(dolls_now, avg)
        standard_deviations.append(variation.sqrt())

print(min(standard_deviations))
