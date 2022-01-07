import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
HO = []
for _ in range(N):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    HO.append((h, o))
D = int(input())

HO.sort(key=lambda x: (x[1], x[0]))

heap = []
ans = 0
for h, o in HO:
    heappush(heap, h)
    while heap and heap[0] < o - D:
        heappop(heap)
    ans = max(len(heap), ans)
print(ans)