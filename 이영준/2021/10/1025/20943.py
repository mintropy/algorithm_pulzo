"""
Title : 카카오톡
Link : https://www.acmicpc.net/problem/20943
"""

import sys
input = sys.stdin.readline


def find_gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


n = int(input())
users = dict()

for _ in range(n):
    a, b, _ = map(int, input().split())
    # 약분하여 튜플로 저장
    gcd = find_gcd(a, b)
    a //= gcd
    b //= gcd
    # a가 무조건 양수 또는 0으로
    if a < 0:
        a *= -1
        b *= -1
    if (a, b) in users:
        users[(a, b)] += 1
    else:
        users[(a, b)] = 1

total_user_set = (n * (n - 1)) // 2
for v in users.values():
    total_user_set -= (v * (v - 1)) // 2

print(total_user_set)


'''
4
4 2 1
2 1 8
6 3 3
1 2 5

'''