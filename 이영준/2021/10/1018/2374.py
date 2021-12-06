"""
Title : 같은 수로 만들기
Link : https://www.acmicpc.net/problem/2374
"""

import sys
input = sys.stdin.readline


def div_conquer(seq_now: list) -> tuple:
    # 지금 seq 구간에서 변환하는 최댓값과 연산수 반환
    # 구간 길이가 2 이하인 경우
    if len(seq_now) == 1:
        return seq_now[0], 0
    elif len(seq_now) == 2:
        return max(seq_now), max(seq_now) - min(seq_now)
    max_num = max(seq_now)
    max_idx = seq_now.index(max_num)
    left_max = right_max = max_num
    left_count = right_count = 0
    if max_idx > 0:
        left_max, left_count = div_conquer(seq_now[:max_idx])
    if max_idx < len(seq_now) - 1:
        right_max, right_count = div_conquer(seq_now[max_idx + 1:])
    return max_num, left_count + right_count + (max_num - left_max) + (max_num - right_max)


n = int(input())
seq = [int(input()) for _ in range(n)]

_, count = div_conquer(seq)
print(count)

'''
7
2
3
1
8
6
7
2
'''