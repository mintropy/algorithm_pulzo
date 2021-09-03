"""
Title : 회의실 배정
Link : https://www.acmicpc.net/problem/1931
"""

import sys
input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
schedule.sort(key= lambda x: (x[1], x[0]))

count = 1
st, end = schedule[0]

for i in range(1, n):
    s, e = schedule[i]
    if s >= end:
        st, end = s, e
        count += 1

print(count)