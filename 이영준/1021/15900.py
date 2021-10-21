"""
Title : 나무 탈출
Link : https://www.acmicpc.net/problem/15900
"""

import sys
input = sys.stdin.readline

n = int(input())

trees = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

# 각 점의 깊이
depth = [0] * (n + 1)
depth[1] = 1
# 잎 노드의 깊이의 합 저장
leaf_depth = 0
stack = [1]

while stack:
    x = stack.pop()
    # 잎 노드
    if x != 1 and len(trees[x]) == 1:
        leaf_depth += depth[x] - 1
        continue
    # 아니라면 순회
    d = depth[x]
    for y in trees[x]:
        if not depth[y]:
            depth[y] = d + 1
            stack.append(y)

if leaf_depth % 2:
    print('Yes')
else:
    print('No')
