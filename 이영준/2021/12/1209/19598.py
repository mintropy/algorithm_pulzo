"""
Title : 최소 회의실 개수
Link : https://www.acmicpc.net/problem/19598
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort()

heap = [0]
count = 1

# for st, end in meetings:
#     if st >= heap[0]:
#         heapq.heappop(heap)
#     else:
#         count += 1
#     heapq.heappush(heap, end)

for st, end in meetings:
    if st >= heap[0]:
        heapq.heappushpop(heap, end)
    else:
        count += 1
        heapq.heappush(heap, end)

print(count)
