import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
S = map(int, input().split())

import heapq
pq = list(S)
heapq.heapify(pq)

for _ in range(M):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    c = a + b
    heapq.heappush(pq, c)
    heapq.heappush(pq, c)

print(sum(pq))