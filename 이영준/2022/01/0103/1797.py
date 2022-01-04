"""
Title : 균형잡힌 줄서기
Link : https://www.acmicpc.net/problem/1797
"""

import sys
input = sys.stdin.readline


N = int(input())
members = [tuple(map(int, input().split())) for _ in range(N)]
members.sort(key=lambda x:x[1])

prefix_sum = [0] * N
for i in range(N):
    if members[i][0] == 0:
        prefix_sum[i] = prefix_sum[i - 1] - 1
    else:
        prefix_sum[i] = prefix_sum[i - 1] + 1

idx_by_prefix_sum:dict = {}
for idx, ps in enumerate(prefix_sum):
    if ps in idx_by_prefix_sum:
        idx_by_prefix_sum[ps].append(idx)
    else:
        idx_by_prefix_sum[ps] = [idx]

if prefix_sum[-1] == 0:
    print(members[-1][1] - members[N % 2][1])
else:
    ans = 0
    for idxs in idx_by_prefix_sum.values():
        left, right = idxs[0], idxs[-1]
        if left == right:
            continue
        tmp = members[right][1] - members[left + 1][1]
        if ans < tmp:
            ans = tmp
    print(ans)
