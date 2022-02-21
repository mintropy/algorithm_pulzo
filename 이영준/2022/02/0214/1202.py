"""
Title : 보석 도둑
Link : https://www.acmicpc.net/problem/1202
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()

jewelries = [tuple(MIIS()) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewelries.sort(key=lambda x: x[0])
bags.sort()

heap = []
value = 0
idx = 0
for bag in bags:
    while idx < N and bag >= jewelries[idx][0]:
        heapq.heappush(heap, -jewelries[idx][1])
        idx += 1
    if heap:
        value += -heapq.heappop(heap)

print(value)
