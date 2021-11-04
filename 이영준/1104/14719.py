"""
Title : 빗물
Link : https://www.acmicpc.net/problem/14719
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


H, W = MIIS()
heights = list(MIIS())

total_water = 0
for i in range(1, max(heights) + 1):
    idx_last = -1
    for j in range(W):
        if heights[j] >= i:
            if idx_last != -1:
                total_water += j - idx_last - 1
            idx_last = j

print(total_water)
