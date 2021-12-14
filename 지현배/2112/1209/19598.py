import heapq
import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key= lambda x: (x[0], x[1]))

idx = 0
queue = []

for n in range(N):
    if queue:
        if queue[0] <= meeting[n][0]:
            heappushpop(queue, meeting[n][1])
        else:
            heappush(queue, meeting[n][1])
    else:
        heappush(queue, meeting[n][1])
print(len(queue))