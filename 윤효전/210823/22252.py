import heapq
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
d = {}
ans = 0
N = int(input())
for _ in range(N):
    t, name, *S = map(lambda x: x.rstrip(), input().split())
    if t == '1':
        K, *S = map(int, S)
        if name in d:
            pq = d[name]
            for n in S:
                heapq.heappush(pq, -n)
        else:
            pq = list(map(lambda x: int(-x), S))
            heapq.heapify(pq)
            d[name] = pq
    else:
        K = int(S[0])
        if name in d:
            pq = d[name]
            if K >= len(pq):
                ans -= sum(pq)
                pq.clear()
            else:
                for _ in range(K):
                    tmp = heapq.heappop(pq)
                    ans -= tmp
print(ans)
