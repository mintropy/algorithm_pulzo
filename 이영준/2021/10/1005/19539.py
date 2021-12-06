"""
Title : 사과나무
Link : https://www.acmicpc.net/problem/19539
"""

import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))

sum_length = sum(trees)
count_2 = sum([i // 2 for i in trees])

if sum_length % 3 == 0 and count_2 >= sum_length // 3:
    print('YES')
else:
    print('NO')


'''
# 비효율적 풀이
import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))

trees_lenght = {i: 0 for i in range(1, 7)}
for i in range(n):
    t = trees[i]
    if t == 0:
        continue
    else:
        t %= 6
        if t == 0:
            t = 6
        trees[i] = t
        trees_lenght[t] += 1


if sum(trees) % 3 != 0:
    print('NO')
else:
    s = sum(trees)
    while s:
        # 최소, 최대 개수
        for i in range(1, 7):
            if trees_lenght[i]:
                min_t = i
                break
        for i in range(6, 0, -1):
            if trees_lenght[i]:
                max_t = i
                break
        if max_t == 1:
            break
        if min_t == max_t and trees_lenght[max_t] == 1:
            break
        count1, count2 = trees_lenght[min_t], trees_lenght[max_t]
        if min_t == max_t:
            count = trees_lenght[min_t] // 2
            s -= count * 3
            trees_lenght[min_t] -= count * 2
            if min_t >= 3:
                trees_lenght[min_t - 2] += count
            if min_t >= 2:
                trees_lenght[min_t - 1] += count
        else:
            if count1 <= count2:
                s -= count1 * 3
                trees_lenght[min_t] -= count1
                trees_lenght[max_t] -= count1
                if min_t != 1:
                    trees_lenght[min_t - 1] += count1
                if max_t != 2:
                    trees_lenght[max_t - 2] += count1
            else:
                s -= count2 * 3
                trees_lenght[min_t] -= count2
                trees_lenght[max_t] -= count2
                if min_t != 1:
                    trees_lenght[min_t - 1] += count2
                if max_t != 2:
                    trees_lenght[max_t - 2] += count2
                    for i in range(max_t - 1, 0, -1):
                        if trees_lenght[i]:
                            max_t = i
    if s:
        print('NO')
    else:
        print('YES')
'''

'''
Counter Example
10
2 2 2 2 2 2 3 4 5 6
ans : YES
'''
