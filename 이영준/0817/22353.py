"""
Title : 헤이카카오
Link : https://www.acmicpc.net/problem/22353
"""

a, d, k = map(int, input().split())
p = d / 100
q = 1
r = 1 + k / 100

estimate = 0
day = a
while True:
    if p >= 1:
        estimate += day * q
        break
    else:
        estimate += day * p * q
        q *= 1 - p
        p *= r
        day += a

print(estimate)
