"""
Title : 정보 상인 호석
Link : https://www.acmicpc.net/problem/22252
"""

import sys, collections
input = sys.stdin.readline


info = collections.defaultdict(list)

total_price = 0

for _ in range(int(input())):
    query = list(input().strip().split())
    # 추가
    if query[0] == '1':
        name = query[1]
        info[name].extend(list(map(int, query[3:])))
    # 구매
    else:
        name = query[1]
        # 구매 개수
        cnt = int(query[2])
        # 원하는 구매개수가 더 많을 때, 모두 구매
        if cnt > len(info[name]):
            total_price += sum(info[name])
            info[name].clear()
        # 아니라면 필요한 개수만큼 구매
        else:
            info[name].sort()
            total_price += sum(info[name][-cnt:])
            for _ in range(cnt):
                info[name].pop()

print(total_price)



'''
# 최적화 하기
import sys, collections, heapq
input = sys.stdin.readline


q = int(input())
info = collections.defaultdict(list)

total_price = 0

for _ in range(q):
    query = list(map(str, input().split()))
    # 추가
    if query[0] == '1':
        name = query[1]
        for p in query[3:]:
            p = int(p)
            heapq.heappush(info[name], (-p, p))
    else:
        name = query[1]
        cnt = int(query[2])
        # 더 많이 구매하면, 모두 꺼내기
        if cnt > len(info[name]):
            for _ in range(len(info[name])):
                _, p = heapq.heappop(info[name])
                total_price += p
        else:
            for _ in range(cnt):
                _, p = heapq.heappop(info[name])
                total_price += p

print(total_price)
'''