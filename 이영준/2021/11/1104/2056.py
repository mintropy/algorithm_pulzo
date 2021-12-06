"""
Title : 작업
Link : https://www.acmicpc.net/problem/2056
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N = int(input())

# 선행되어야 할 일
pre_works = [[]]
# 후행 작업 확인
post_works = [[] for _ in range(N + 1)]
# 위상 정렬 / 선행 작업이 없는 모든 작업 추가
queue = deque([])
for i in range(1, N + 1):
    t, w, *work_list = MIIS()
    # 선행 작업 없을 때
    if not w:
        queue.append((0, i))
    # 선행 작업 확인은 선행 작업 완료 갯수로 확인 + 최소 시작 시간
    pre_works.append([t, w, 0])
    # 후행 작업 확인은 해당 일 인덱스 넣어서
    for work in work_list:
        post_works[work].append(i)

# 작업 시간 확인
time = 0
while queue:
    t0, idx = queue.popleft()
    # 작업 시작 시간 확인
    if t0 < pre_works[idx][2]:
        t0 = pre_works[idx][2]
    # 최대 작업 시간 확인
    t1 = pre_works[idx][0]
    if time < t0 + t1:
        time = t0 + t1
    # 후행 작업 확인
    post_works[idx].sort()
    for work in post_works[idx]:
        pre_works[work][1] -= 1
        if not pre_works[work][1]:
            queue.append((t0 + t1, work))
        elif pre_works[work][2] < t0 + t1:
            pre_works[work][2] = t0 + t1

print(time)


'''
Counter Example
7
5 0
1 0
3 0
6 0
1 0
8 0
4 0
ans : 8

5
6 0
3 0
3 2 1 2
1 1 1
1 2 3 4
ans : 10
'''
