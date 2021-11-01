"""
Title : 인형들
Link : https://www.acmicpc.net/problem/15954
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def calc_variation(nums: list, avg: int) -> int:
    variation = 0
    for num in nums:
        variation += (num - avg) ** 2
    return variation / len(dolls_now)


N, K = MIIS()
dolls = list(MIIS())

standard_deviations = []

for i in range(N - K + 1):
    # K개 이상 연속 확인
    for j in range(i + K, N + 1):
        dolls_now = dolls[i:j]
        avg = sum(dolls_now) / len(dolls_now)
        variation = calc_variation(dolls_now, avg)
        standard_deviations.append(variation ** 0.5)

print(min(standard_deviations))
