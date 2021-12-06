"""
Title : 카드 합체 놀이
Link : https://www.acmicpc.net/problem/15903
"""

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x + y)
    heapq.heappush(heap, x + y)

print(sum(heap))