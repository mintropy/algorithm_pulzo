"""
Title : 블록 쌓기
Link : https://www.acmicpc.net/problem/9998
"""

import sys
input = sys.stdin.readline


def ternary_search():
    global n, yoon, dong
    min_cost = 4 * 10 ** 17
    left, right = max((0, min((min(yoon), min(dong))) - 1)), max((max(yoon), max(dong)))
    while left <= right:
        third = (right - left) // 3
        one_of_third, two_of_third = left + third, left + (2 * third)
        ans1 = list(range(one_of_third + n // 2, one_of_third, -1)) + [one_of_third] + list(range(one_of_third + 1, one_of_third + n // 2 + 1))
        ans2 = list(range(two_of_third + n // 2, two_of_third, -1)) + [two_of_third] + list(range(two_of_third + 1, two_of_third + n // 2 + 1))
        move1 = sum(list(abs(yoon[i] - ans1[i]) for i in range(n))) +  sum(list(abs(dong[i] - ans1[i]) for i in range(n)))
        move2 = sum(list(abs(yoon[i] - ans2[i]) for i in range(n))) +  sum(list(abs(dong[i] - ans2[i]) for i in range(n)))
        # 최솟값 갱신 & 삼분위치 탐색
        if move1 <= move2:
            # if min_cost == -1:
            #     min_cost = move1
            if move1 < min_cost:
                min_cost = move1
            right = two_of_third - 1
        else:
            # if min_cost == -1:
            #     min_cost = move2
            if move2 < min_cost:
                min_cost = move2
            left = one_of_third + 1
    return min_cost


n = int(input())
yoon = list(map(int, input().split()))
dong = list(map(int, input().split()))

print(ternary_search())


'''
Counter Example
5
3 2 5 2 3
3 2 4 2 3
ans : 7

'''