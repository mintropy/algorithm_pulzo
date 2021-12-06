"""
Title : 동작 그만. 밑장 빼기냐?
Link : https://www.acmicpc.net/problem/20159
"""

import sys
input = sys.stdin.readline


n = int(input())
cards = list(map(int, input().split()))

prefix_sum_first = [cards[-2]]
prefix_sum_second = [cards[-1]]

for i in range(n - 3, -1, -1):
    if i % 2:
        prefix_sum_second.append(prefix_sum_second[-1] + cards[i])
    else:
        prefix_sum_first.append(prefix_sum_first[-1] + cards[i])
prefix_sum_first.append(prefix_sum_first[-1])
prefix_sum_second.append(prefix_sum_second[-1])

prefix_sum_first.reverse()
prefix_sum_second.reverse()

max_sum = prefix_sum_first[0]

# i번 째 및장빼기 할 때
for i in range(n - 1):
    # 상대방 차례
    if i % 2:
        if max_sum < (prefix_sum_first[0] - prefix_sum_first[i // 2 + 2]) + (prefix_sum_second[i // 2 + 1] - prefix_sum_second[-1]):
            max_sum = (prefix_sum_first[0] - prefix_sum_first[i // 2 + 2]) + (prefix_sum_second[i // 2 + 1] - prefix_sum_second[-1])
    # 정훈이 차례
    else:
        if max_sum < (prefix_sum_first[0] - prefix_sum_first[i // 2 + 1]) + cards[-1] + (prefix_sum_second[i // 2 + 1] - prefix_sum_second[-1]):
            max_sum = (prefix_sum_first[0] - prefix_sum_first[i // 2 + 1]) + cards[-1] + (prefix_sum_second[i // 2 + 1] - prefix_sum_second[-1])

print(max_sum)

'''
Conter Example
8
2 1 1 1 2 2 1 1
ans : 7
out : 6
'''
