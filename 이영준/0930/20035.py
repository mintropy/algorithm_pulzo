"""
Title : 이동하기 5
Link : https://www.acmicpc.net/problem/20035
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n, m = MIIS()
A = list(MIIS())
B = list(MIIS())

# 사탕 개수 중 a_i에 들어갈 수 탐색
max_a_i = max(A)
sum_a_i = sum(A) + max_a_i * (m - 1)

# a_i중 가장 큰 수가 유일한지, 아니면 가장 위, 아래 인덱스
if A.count(max_a_i) == 1:
    up = down = A.index(max_a_i)
else:
    up = A.index(max_a_i)
    down = n - A[::-1].index(max_a_i) - 1

# 사탕 개수 중 b_i에 들어갈 수 탐색
max_b_i = max(B)
sum_b_i = sum(B)

# 추가적 길 탐색
sum_b_i += B[0] * (up)
sum_b_i += max_b_i * (down - up)
sum_b_i += B[-1] * (n - down - 1)

print(sum_a_i * 10 ** 9 + sum_b_i)
