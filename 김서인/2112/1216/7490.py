# import copy
# import sys
#
# input = sys.stdin.readline
# MIIS = lambda: map(int, input().strip().split())
#
#
# def dfs(idx, curr_num, history):
#     global ans
#     if idx == N + 1:  # 끝까지 옴
#         tmp = ''.join(map(str, history)).replace(' ', '')  # 결과식(숫자 붙임)
#         if eval(tmp) == 0:  # 결과가 0이 된다면
#             ans.append(''.join(map(str, history)))
#         return
#
#     history_copy1 = copy.copy(history)
#     history_copy1.extend(['+', idx])
#     dfs(idx + 1, curr_num + idx, history_copy1)
#
#     history_copy2 = copy.copy(history)
#     history_copy2.extend(['-', idx])
#     dfs(idx + 1, curr_num - idx, history_copy2)
#
#     history_copy3 = copy.copy(history)
#     t = history_copy3[-1]
#     tmp = t * 10 + idx - t
#     history_copy3.extend([' ', idx])
#     dfs(idx + 1, tmp, history_copy3)
#
#
# T = int(input().strip())
# for _ in range(T):
#     N = int(input().strip())
#     ans = []
#     dfs(2, 1, [1])
#     ans.sort()
#     for a in ans:
#         print(a)
#     print()

import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().strip().split())


def dfs(idx, history):
    global ans
    if idx == N + 1:  # 끝까지 옴
        tmp = history.replace(' ', '')  # 결과식(숫자 붙임)
        if eval(tmp) == 0:  # 결과가 0이 된다면
            ans.append(history)
        return

    dfs(idx + 1,  history+f'+{idx}')

    dfs(idx + 1,  history+f'-{idx}')

    dfs(idx + 1, history+f' {idx}')


T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    ans = []
    dfs(2, '1')
    ans.sort()
    for a in ans:
        print(a)
    print()