"""
Title : 가장 가까운 공통 조상
Link : https://www.acmicpc.net/problem/3584
"""

import sys
import collections
input = sys.stdin.readline


def find_parent():
    global parent, child, depth
    # 루트 찾기
    for i in range(1, n + 1):
        if not parent[i]:
            root = i
            break
    # 루트로부터 깊이, 부모 설정
    queue = collections.deque([root])
    depth[root] = 1
    while queue:
        p = queue.popleft()
        queue.extend(child[p])
        # 인접한 점을 자식으로 설정
        for q in child[p]:
            d = depth[q] = depth[p] + 1
            i = 0
            while (d + 1) - (2 ** i) > 0:
                if parent[q][-1] == 1:
                    break
                try:
                    parent[q].append(parent[parent[q][i]][i])
                    i += 1
                except:
                    break


def LCA(a, b):
    # b 깊이가 더 깊거나 같도록
    if depth[a] > depth[b]:
        a, b = b, a
    # 높이 맞춰주기
    while depth[a] < depth[b]:
        for b_ in parent[b][::-1]:
            if depth[b_] == depth[a]:
                b = b_
                break
            elif depth[b_] > depth[a]:
                b = b_
                break
    if a == b:
        return a
    # 공통 조상 찾아가기
    while a != b:
        for i in range(len(parent[a]) - 1, 0, -1):
            if parent[a][i] != parent[b][i]:
                a, b = parent[a][i], parent[b][i]
                break
        else:
            a, b = parent[a][0], parent[b][0]
    return a


for _ in range(int(input())):
    n = int(input())
    # 2^i 번째 부모
    parent = [[] for _ in range(n + 1)]
    # 자식
    child = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        child[a].append(b)
        parent[b].append(a)

    # 깊이
    depth = [0] * (n + 1)
    find_parent()

    a, b = map(int, input().split())
    print(LCA(a, b))
