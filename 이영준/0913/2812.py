"""
Title : 크게 만들기
Link : https://www.acmicpc.net/problem/2812
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(int(i) for i in input().strip())

stack = []
count = 0
# 사용하지 않는 개수가 가능한 만큼, 왼쪽으로 넣기
for m in num:
    while stack and stack[-1] < m and count < k:
        stack.pop()
        count += 1
    stack.append(m)

while count < k:
    stack.pop()
    count += 1

print(*stack, sep='')
