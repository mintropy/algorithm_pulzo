"""
Title : 싸지방에 간 준하
Link : https://www.acmicpc.net/problem/12764
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
schedual = [tuple(map(int, input().split())) for _ in range(n)]
# 시작시간 오름차순 정렬
schedual.sort(key=lambda x:x[0])

# 지금 싸지방 사용하는 사람의 종료 시간
ssa_ji_bang = []
# 놀고있는 컴퓨터
sleeping_pc = []
# 각 컴퓨터를 몇 명이 하는지
pc_per_person = [0] * n

# 지금 최대로 사용한 pc 대수
pc_idx = 0

for st, end in schedual:
    # 싸지방 사용하는 사람 있을 때
    if ssa_ji_bang:
        # 더 빨리 종요하는 사람 있으면 모두 퇴장
        while ssa_ji_bang and ssa_ji_bang[0][0] <= st:
            _, idx = heapq.heappop(ssa_ji_bang)
            heapq.heappush(sleeping_pc, idx)
    # 다음 사람 싸지방에 넣기
    # 놀고 있는 컴퓨터 있으면 해당 컴퓨터로
    # 없으면 사람수에 해당하는 컴퓨터로
    if sleeping_pc:
        idx = heapq.heappop(sleeping_pc)
    else:
        idx = len(ssa_ji_bang)
    pc_per_person[idx] += 1
    heapq.heappush(ssa_ji_bang, (end, idx))
    # 사용 pc대수 확인
    if len(ssa_ji_bang) > pc_idx:
        pc_idx = len(ssa_ji_bang)

print(pc_idx)
print(*pc_per_person[:pc_idx])


'''
# python TLE
import sys, heapq
input = sys.stdin.readline

n = int(input())
schedual = [tuple(map(int, input().split())) for _ in range(n)]
# 시작시간 오름차순 정렬
schedual.sort(key=lambda x:x[0])

# 지금 싸지방 사용하는 사람의 종료 시간
heap = []
# 각 사람이 사용하는 컴퓨터 번호
pc_num = [1] * n
# 각 i번 pc를 사용한 사람 수
pc_count = [0] * (n + 1)
# 비어있는 pc
empty_pc = set()
for idx, (st, end) in enumerate(schedual):
    # 사용중인 컴퓨터가 없을 때
    if not heap:
        pc_num[idx] = 1
        pc_count[1] += 1
        heapq.heappush(heap, (end, 1))
    # 사용중인 컴퓨터가 있을 때
    else:
        # 다음 사용자 입장시간 st와 heap[0] 비교
        # heap[0]가 더 작거나 같을 때 pop
        while heap and heap[0][0] <= st:
            _, i = heapq.heappop(heap)
            empty_pc.add(i)
        if empty_pc:
            pc_now = min(empty_pc)
            empty_pc.remove(pc_now)
            pc_num[idx] = pc_now
            pc_count[pc_now] += 1
            heapq.heappush(heap, (end, pc_now))
        else:
            pc_num[idx] = len(heap) + 1
            pc_count[len(heap) + 1] += 1
            heapq.heappush(heap, (end, len(heap) + 1))

max_pc = max(pc_num)
print(max_pc)
for i in range(1, max_pc + 1):
    print(pc_count[i], end=' ')
'''

'''
# TLE
import sys, heapq
input = sys.stdin.readline

n = int(input())
schedual = [tuple(map(int, input().split())) for _ in range(n)]
# 시작시간 오름차순 정렬
schedual.sort(key=lambda x:x[0])

# 사용자를 앞에서부터 채웠을 때
heap = []
# 비어있는 pc
empty_pc = []
# idx번째 사용자가 몇번 컴퓨터를 사용하는지
# 기본은 0번 컴퓨터 사용
pc_num = [0] * n
for idx, (st, end) in enumerate(schedual):
    # 사용중인 컴퓨터가 없을 때
    if not heap:
        heapq.heappush(heap, (end, 0))
    # 사용중인 컴퓨터가 있을 때
    else:
        # 다음 사용자 입장시간 st와 heap[0] 비교
        # heap[0]가 더 작거나 같을 때 pop
        while heap and heap[0][0] <= st:
            _, i = heapq.heappop(heap)
            heapq.heappush(empty_pc, i)
        if empty_pc:
            pc_now = heapq.heappop(empty_pc)
            pc_num[idx] = pc_now
            heapq.heappush(heap, (end, pc_now))
        else:
            pc_num[idx] = len(heap)
            heapq.heappush(heap, (end, len(heap)))

max_pc = max(pc_num)
print(max_pc + 1)
for i in range(max_pc + 1):
    print(pc_num.count(i), end=' ')
'''
