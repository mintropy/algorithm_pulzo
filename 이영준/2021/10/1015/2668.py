"""
Title : 숫자고르기
Link : https://www.acmicpc.net/problem/2668
"""

import sys
input = sys.stdin.readline


def dfs(set_up, set_down, num_now):
    global seq, disjoint_set, used
    if set_up == set_down:
        disjoint_set.append(set_up)
        for x in set_up:
            used[x] = True
        return
    # 사용한 숫자일때
    if used[num_now]:
        return
    # 같은 숫자만 재귀될때
    if num_now == seq[num_now] or num_now in set_up or seq[num_now] in set_down:
        return
    dfs(set_up | {num_now}, set_down | {seq[num_now]}, seq[num_now])


n = int(input())
seq = [0] + [int(input()) for _ in range(n)]

# 해당 숫자가 사용됬는지
used = [False] * (n + 1)
# 각각의 서로소 집합으로
disjoint_set = []

for i in range(1, n + 1):
    if not used[i]:
        dfs({i}, {seq[i]}, seq[i])

ans = sorted(sum(map(list, disjoint_set), start=[]))
print(len(ans), *ans, sep='\n')
