from heapq import *
import sys
input = sys.stdin.readline
Q = int(input())
sum = 0
infos = {}
for _ in range(Q):
    [query, name, k, *C] = input().split()
    k = int(k)
    C = list(map(int, C))
    # 고릴라의 정보 획득
    if query == '1':
        if not name in infos:
            infos[name] = []
        for _ in range(k):
            heappush(infos[name], -C.pop())
    # 호석이의 정보 구입
    else:
        if name in infos:
            if k > len(infos[name]): k = len(infos[name])
            for _ in range(k):
                sum -= heappop(infos[name])
print(sum)