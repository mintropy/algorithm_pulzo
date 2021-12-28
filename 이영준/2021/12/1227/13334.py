"""
Title : 철로
Link : https://www.acmicpc.net/problem/13334
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
people = []
for _ in range(N):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    people.append((h, o))
D = int(input())

people.sort(key=lambda x:x[1])
max_count = 0
idx = 0
heap = []

while True:
    while idx < N:
        if people[idx][1] - people[idx][0] > D:
            idx += 1
            continue
        elif not heap:
            heapq.heappush(heap, people[idx])
            idx += 1
        elif heap[0][0] + D >= people[idx][1]:
            heapq.heappush(heap, people[idx])
            idx += 1
        else:
            break
    if max_count < len(heap):
        max_count = len(heap)
    if heap:
        st = heap[0][0]
        while heap:
            if heap[0][0] == st:
                heapq.heappop(heap)
            else:
                break
    else:
        break

print(max_count)
