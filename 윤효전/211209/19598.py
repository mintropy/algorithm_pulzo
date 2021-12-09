import sys
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x:x[0])
pq = []

ans = 0

i = 0
while i < len(S):
    start, end = S[i]
    if len(pq) == 0:
        heapq.heappush(pq, (end, start))
    else:
        top_start, top_end = pq[0][1], pq[0][0]
        if top_end > start:
            heapq.heappush(pq, (end, start))
        else:
            heapq.heappop(pq)
            continue
    ans = max(ans, len(pq))
    i += 1
    
print(ans)
