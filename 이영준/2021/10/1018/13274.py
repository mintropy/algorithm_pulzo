"""
Title : 수열
Link : https://www.acmicpc.net/problem/13274
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n, k = MIIS()
seq = sorted(list(MIIS()))

for _ in range(k):
    l, r, x = MIIS()
    for i in range(l - 1, r):
        seq[i] += x
    seq.sort()

print(*seq)

'''
for _ in range(k):
    l, r, x = MIIS()
    if x == 0:
        continue
    elif x > 0:
        stack = []
        for i in range(r - 1, l - 2, -1):
            stack.append(seq[i] + x)
        idx = l - 1
        right = r
        while right < n and idx < n and stack:
            if stack[-1] <= seq[right]:
                seq[idx] = stack.pop()
            else:
                seq[idx] = seq[right]
                right += 1
            idx += 1
        while stack:
            seq[idx] = stack.pop()
            idx += 1
    else:
        stack = []
        for i in range(l - 1, r):
            stack.append(seq[i] + x)
        idx = r - 1
        left = l - 2
        while 0 <= left and 0 <= idx and stack:
            if stack[-1] >= seq[left]:
                seq[idx] = stack.pop()
            else:
                seq[idx] = seq[left]
                left -= 1
            idx -= 1
        while stack:
            seq[idx] = stack.pop()
            idx -= 1

print(*seq)
'''

'''
Counter Example
10 1
1 2 3 4 5 6 7 8 9 10
3 6 3

'''
