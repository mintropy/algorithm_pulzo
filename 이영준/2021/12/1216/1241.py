"""
Title : 머리 톡톡
Link : https://www.acmicpc.net/problem/1241
"""

import sys
input = sys.stdin.readline


N = int(input())

head = []
count = {}
result = {}

for _ in range(N):
    H = int(input())
    head.append(H)
    if H in count:
        count[H] += 1
    else:
        count[H] = 1

for H, cnt in count.items():
    for i in range(H, 1_000_001, H):
        if i in count:
            if i in result:
                result[i] += cnt
            else:
                result[i] = cnt

for H in head:
    print(result[H] - 1)


'''
N = int(input())

head = []
nums = [0] * 100_000_1
result = [0] * 100_000_1
for _ in range(N):
    H = int(input())
    head.append(H)
    nums[H] += 1

for i in range(1, max(head) + 1):
    num = nums[i]
    if num:
        for j in range(i, max(head) + 1, i):
            result[j] += num

for H in head:
    print(result[H] - 1)
'''
