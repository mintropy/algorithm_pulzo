"""
Title : 문제 추천 시스템 Version 1
Link : https://www.acmicpc.net/problem/21939
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
questions = dict()
heap_asc = []
heap_des = []
for _ in range(N):
    p, l = map(int, input().split())
    questions[p] = True
    heap_asc.append((l, p))
    heap_des.append((-l, -p))
heapq.heapify(heap_asc)
heapq.heapify(heap_des)

for _ in range(int(input())):
    cmd, *todo = input().strip().split()
    if cmd == 'recommend':
        x = int(todo[0])
        if x == 1:
            while not questions[-heap_des[0][1]]:
                heapq.heappop(heap_des)
            print(-heap_des[0][1])
        else:
            while not questions[heap_asc[0][1]]:
                heapq.heappop(heap_asc)
            print(heap_asc[0][1])
    elif cmd == 'add':
        p, l = map(int, todo)
        while not questions[heap_asc[0][1]]:
            heapq.heappop(heap_asc)
        while not questions[-heap_des[0][1]]:
            heapq.heappop(heap_des)
        questions[p] = True
        heapq.heappush(heap_asc, (l, p))
        heapq.heappush(heap_des, (-l, -p))
    elif cmd == 'solved':
        p = int(todo[0])
        questions[p] = False

'''
Counter Example
# 반례가 있긴한데 아직은 통과되는듯
3
1000 1
2000 37
3000 55
4
solved 2000
add 2000 70
solved 1000
recommend -1

ans : 3000
'''
