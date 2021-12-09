"""
Title : 커피숍2
Link : https://www.acmicpc.net/problem/1275
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


# 처음 값 설정
def init(start, end, node):
    global seq, segment_tree
    if start == end:
        segment_tree[node] = seq[start]
        return seq[start]
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

# 부분합
def partial_sum(start, end, node, left, right):
    global segment_tree
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return partial_sum(start, mid, node * 2, left, right) + partial_sum(mid + 1, end, node * 2 + 1, left, right)

# 값 변경
def update(start, end, node, idx, dif):
    global segment_tree
    if idx < start or idx > end:
        return
    segment_tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, dif)
    update(mid + 1, end, node * 2 + 1, idx, dif)

def solution(N, Q):
    init(1, N, 1)
    for _ in range(Q):
        x, y, a, b = MIIS()
        if x > y:
            x, y = y, x
        print(partial_sum(1, N, 1, x, y))
        update(1, N, 1, a, b - seq[a])
        seq[a] = b


N, Q = MIIS()
seq = [0] + list(MIIS())

segment_tree = [0 for _ in range(N * 4)]
solution(N, Q)
