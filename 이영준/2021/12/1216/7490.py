"""
Title : 0 만들기
Link : https://www.acmicpc.net/problem/7490
"""

import sys
input = sys.stdin.readline


def dfs(comb_now : str, comb_list: list, idx: int, target: int):
    global tmp
    if idx == target + 1:
        if sum(comb_list) == 0:
            tmp += comb_now + '\n'
        return
    
    # dfs(comb_now + f' {idx}', comb_list[:-1] + [int(str(comb_list[-1]) + str(idx))], idx + 1, target)
    if comb_list[-1] < 0:
        dfs(comb_now + f' {idx}', comb_list[:-1] + [comb_list[-1] * 10 - idx], idx + 1, target)
    else:
        dfs(comb_now + f' {idx}', comb_list[:-1] + [comb_list[-1] * 10 + idx], idx + 1, target)
    dfs(comb_now + f'+{idx}', comb_list + [idx], idx + 1, target)
    dfs(comb_now + f'-{idx}', comb_list + [-idx], idx + 1, target)


TC = int(input())
ans_for_num = {}
nums = [int(input()) for _ in range(TC)]

for i in set(nums):
    tmp = ''
    dfs('1', [1], 2, i)
    ans_for_num[i] = tmp

ans = ''
for i in nums:
    ans += ans_for_num[i] + '\n'
print(ans)


'''
# even slower
import sys
input = sys.stdin.readline


def dfs(comb_now : str, idx: int, target: int):
    if idx == target + 1:
        if verify(comb_now):
            print(comb_now)
        return
    dfs(comb_now + ' ' + str(idx), idx + 1, target)
    dfs(comb_now + '+' + str(idx), idx + 1, target)
    dfs(comb_now + '-' + str(idx), idx + 1, target)


def verify(comb: str) -> bool:
    eq = ''
    for s in comb:
        if s == ' ':
            continue
        eq += s
    if eval(eq) == 0:
        return True
    return False


for _ in range(int(input())):
    dfs('1', 2, int(input()))
    print()
'''
